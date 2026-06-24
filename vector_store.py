from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pickle
import os


class VectorStore:

    def __init__(self):

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

    def create_index(self, chunks):

        embeddings = self.model.encode(chunks)

        embeddings = np.array(
            embeddings,
            dtype="float32"
        )

        dimension = embeddings.shape[1]

        index = faiss.IndexFlatL2(
            dimension
        )

        index.add(embeddings)

        return index

    def save_user_data(
        self,
        user_id,
        index,
        chunks
    ):

        user_folder = (
            f"user_data/{user_id}"
        )

        os.makedirs(
            user_folder,
            exist_ok=True
        )

        faiss.write_index(
            index,
            f"{user_folder}/faiss.index"
        )

        with open(
            f"{user_folder}/chunks.pkl",
            "wb"
        ) as f:

            pickle.dump(
                chunks,
                f
            )

    def load_user_data(
        self,
        user_id
    ):

        user_folder = (
            f"user_data/{user_id}"
        )

        index_path = (
            f"{user_folder}/faiss.index"
        )

        chunks_path = (
            f"{user_folder}/chunks.pkl"
        )

        if (
            not os.path.exists(index_path)
            or not os.path.exists(chunks_path)
        ):
            return None, None

        index = faiss.read_index(
            index_path
        )

        with open(
            chunks_path,
            "rb"
        ) as f:

            chunks = pickle.load(f)

        return index, chunks

    def search(
        self,
        question,
        index,
        chunks,
        k=5
    ):

        query_embedding = self.model.encode(
            [question]
        )

        query_embedding = np.array(
            query_embedding,
            dtype="float32"
        )

        distances, indices = index.search(
            query_embedding,
            min(k, len(chunks))
        )

        retrieved_chunks = []

        for idx in indices[0]:

            if (
                idx >= 0
                and idx < len(chunks)
            ):
                retrieved_chunks.append(
                    chunks[idx]
                )

        return retrieved_chunks