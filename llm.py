from mistralai.client import Mistral
from dotenv import load_dotenv
import os

load_dotenv()


class LLMService:

    def __init__(self):

        self.client = Mistral(
            api_key=os.getenv("MISTRAL_API_KEY")
        )

    def generate(self, prompt):

        response = self.client.chat.complete(
            model="mistral-small-latest",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content