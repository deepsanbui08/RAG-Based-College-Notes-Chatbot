import os

from dotenv import load_dotenv

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

from pdf_processor import process_pdf
from vector_store import VectorStore
from rag_pipeline import answer_question


load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Store user data in memory
USER_DATA = {}


async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    await update.message.reply_text(
        "📚 Welcome to College Notes AI!\n\n"
        "Upload a PDF file and then ask questions about it."
    )


async def help_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    await update.message.reply_text(
        "/start - Start the bot\n"
        "/help - Show commands\n"
        "/reset - Delete uploaded notes"
    )


async def reset_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    user_id = update.effective_user.id

    if user_id in USER_DATA:

        del USER_DATA[user_id]

        await update.message.reply_text(
            "✅ Notes removed successfully.\nUpload a new PDF."
        )

    else:

        await update.message.reply_text(
            "No uploaded notes found."
        )


async def handle_pdf(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    try:

        user_id = update.effective_user.id

        document = update.message.document

        if not document.file_name.lower().endswith(".pdf"):

            await update.message.reply_text(
                "Please upload a PDF file."
            )

            return

        await update.message.reply_text(
            "📄 Processing PDF..."
        )

        pdf_path = f"temp_{user_id}.pdf"

        telegram_file = await document.get_file()

        await telegram_file.download_to_drive(
            pdf_path
        )

        chunks = process_pdf(
            pdf_path
        )

        if not chunks:

            await update.message.reply_text(
                "Could not extract text from PDF."
            )

            return

        vector_store = VectorStore()

        index = vector_store.create_index(
            chunks
        )

        USER_DATA[user_id] = {
            "chunks": chunks,
            "index": index
        }

        # remove temporary file
        if os.path.exists(pdf_path):
            os.remove(pdf_path)

        await update.message.reply_text(
            f"✅ PDF processed successfully!\n\n"
            f"Chunks created: {len(chunks)}\n\n"
            f"You can now ask questions."
        )

    except Exception as e:

        await update.message.reply_text(
            f"Error processing PDF:\n{e}"
        )


async def handle_question(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    try:

        user_id = update.effective_user.id

        if user_id not in USER_DATA:

            await update.message.reply_text(
                "Please upload a PDF first."
            )

            return

        question = update.message.text

        await update.message.reply_text(
            "🤖 Thinking..."
        )

        chunks = USER_DATA[user_id]["chunks"]

        index = USER_DATA[user_id]["index"]

        answer = answer_question(
            question,
            chunks,
            index
        )

        await update.message.reply_text(
            answer
        )

    except Exception as e:

        await update.message.reply_text(
            f"Error:\n{e}"
        )


def main():

    app = (
        ApplicationBuilder()
        .token(TOKEN)
        .build()
    )

    app.add_handler(
        CommandHandler(
            "start",
            start
        )
    )

    app.add_handler(
        CommandHandler(
            "help",
            help_command
        )
    )

    app.add_handler(
        CommandHandler(
            "reset",
            reset_command
        )
    )

    app.add_handler(
        MessageHandler(
            filters.Document.PDF,
            handle_pdf
        )
    )

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            handle_question
        )
    )

    print("🚀 Bot is running...")

    app.run_polling()


if __name__ == "__main__":
    main()

