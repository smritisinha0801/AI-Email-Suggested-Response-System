import os
from dotenv import load_dotenv
import google.generativeai as genai

from services.retrieve import EmailRetriever
from services.evaluator import ResponseEvaluator
from services.prompts import build_prompt

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("models/gemini-2.5-flash")

class EmailGenerator:

    def __init__(self):
        self.retriever = EmailRetriever()
        self.evaluator = ResponseEvaluator()

    def generate_reply(self, customer_email):

        retrieved = self.retriever.retrieve(customer_email, top_k=3)

        prompt = build_prompt(customer_email, retrieved)

        response = model.generate_content(prompt)

        ai_reply = response.text

        scores = self.evaluator.evaluate(
            ai_reply,
            retrieved[0]["human_response"]
        )

        return ai_reply, retrieved, scores


if __name__ == "__main__":

    generator = EmailGenerator()

    customer_email = input("Enter customer email:\n\n")

    reply, retrieved, scores = generator.generate_reply(customer_email)

    print("\n")
    print("=" * 70)
    print("AI GENERATED RESPONSE")
    print("=" * 70)
    print(reply)

    print("\n")
    print("=" * 70)
    print("TOP RETRIEVED EMAILS")
    print("=" * 70)

    for i, item in enumerate(retrieved, start=1):
        print(f"{i}. {item['customer_email']}")

    print("\n")
    print("=" * 70)
    print("EVALUATION")
    print("=" * 70)

    for k, v in scores.items():
        print(f"{k}: {v}")