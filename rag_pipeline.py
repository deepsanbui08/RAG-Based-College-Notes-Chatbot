from llm import LLMService
from vector_store import VectorStore
import re


def clean_response(text):

    text = re.sub(r"\*\*", "", text)
    text = re.sub(r"\*", "", text)
    text = re.sub(r"#+", "", text)
    text = re.sub(r"`", "", text)

    return text.strip()


def answer_question(
    question,
    chunks,
    index
):

    vector_store = VectorStore()

    retrieved_chunks = vector_store.search(
        question,
        index,
        chunks
    )

    context = "\n\n".join(
        retrieved_chunks
    )

    prompt = f"""
    Answer using only the provided context.

    Use plain text only.

    Context:
    {context}

    Question:
    {question}

    Answer:
    """

    llm = LLMService()

    answer = llm.generate(prompt)

    return clean_response(answer)