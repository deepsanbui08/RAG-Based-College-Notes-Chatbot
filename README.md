# 📚 College Notes AI Telegram Bot

An AI-powered Telegram chatbot that allows users to upload PDF notes and ask questions about their content using Retrieval-Augmented Generation (RAG).

The bot extracts text from uploaded PDFs, generates embeddings using Sentence Transformers, stores them in a FAISS vector database, retrieves relevant information based on user queries, and generates answers using Mistral AI.

---

## 🚀 Features

* Upload PDF notes directly through Telegram
* Ask questions about uploaded documents
* Retrieval-Augmented Generation (RAG)
* Semantic search using FAISS
* Sentence Transformers for embeddings
* Mistral AI for answer generation
* Multi-user support
* Session reset functionality

---

## 🏗️ Project Architecture

```text
User
 │
 ▼
Telegram Bot
 │
 ▼
PDF Upload
 │
 ▼
Text Extraction
 │
 ▼
Chunking
 │
 ▼
Sentence Transformers
 │
 ▼
FAISS Vector Store
 │
 ▼
Relevant Context Retrieval
 │
 ▼
Mistral AI
 │
 ▼
Answer
```

---

## 📂 Project Structure

```text
RAG-Based-College-Notes-Chatbot/
│
├── requirements.txt
├── README.md
├── .env
│
└── project_files/
    ├── telegram_bot.py
    ├── llm.py
    ├── pdf_processor.py
    ├── vector_store.py
    └── rag_pipeline.py
```

---

## 🛠️ Technologies Used

* Python
* Telegram Bot API
* Mistral AI
* FAISS
* Sentence Transformers
* LangChain Text Splitters
* PyPDF2
* NumPy
* python-dotenv

---

## ⚙️ Installation

### Clone Repository

```bash
git clone <repository-url>
cd RAG-Based-College-Notes-Chatbot
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
MISTRAL_API_KEY=your_mistral_api_key
```

---

## ▶️ Run Locally

```bash
python project_files/telegram_bot.py
```

---

## 📖 How to Use

1. Start the bot on Telegram.
2. Upload a PDF document.
3. Wait for the PDF to be processed.
4. Ask questions related to the uploaded document.
5. Use `/reset` to clear the current session and upload a new PDF.

---

## 🤖 Commands

| Command | Description                                |
| ------- | ------------------------------------------ |
| /start  | Start the bot                              |
| /help   | Show help information                      |
| /reset  | Remove current PDF and start a new session |

---

## 💡 Example Queries

* What is polymorphism?
* Explain blockchain consensus.
* Summarize chapter 3.
* What are the advantages of IoT?
* List the key points from Unit 4.

---

## 📌 Limitations

* One PDF is active per user session.
* PDF data is stored in memory.
* Uploaded PDFs are cleared when the bot restarts.

---

## 🔮 Future Improvements

* Multiple PDF support
* Quiz generation
* Flashcard generation
* PDF summaries
* Source citations
* Persistent vector database
* Cloud deployment

---

## 👨‍💻 Author

Deep Sanbui


