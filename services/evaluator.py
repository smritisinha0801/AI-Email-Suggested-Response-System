import numpy as np
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
from rouge_score import rouge_scorer
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


class ResponseEvaluator:

    def __init__(self):
        print("Loading evaluation model...")
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

        self.rouge = rouge_scorer.RougeScorer(
            ['rougeL'],
            use_stemmer=True
        )

    def evaluate(self, generated_response, reference_response):

        # ---------------- BLEU ---------------- #

        smoothie = SmoothingFunction().method1

        bleu = sentence_bleu(
            [reference_response.split()],
            generated_response.split(),
            smoothing_function=smoothie
        )

        # ---------------- ROUGE ---------------- #

        rouge = self.rouge.score(
            reference_response,
            generated_response
        )["rougeL"].fmeasure

        # ---------------- Cosine Similarity ---------------- #

        embeddings = self.model.encode(
            [generated_response, reference_response]
        )

        cosine = cosine_similarity(
            [embeddings[0]],
            [embeddings[1]]
        )[0][0]

        return {
            "BLEU": round(float(bleu), 4),
            "ROUGE-L": round(float(rouge), 4),
            "Cosine Similarity": round(float(cosine), 4)
        }


if __name__ == "__main__":

    generated = """
Dear Customer,

We're sorry for the delay.
Your refund is being processed and should arrive within 3-5 business days.

Best Regards,
Support Team
"""

    reference = """
We're sorry for the delay.
Your refund is currently being processed and should reach your account within 3-5 business days.
"""

    evaluator = ResponseEvaluator()

    scores = evaluator.evaluate(
        generated,
        reference
    )

    print("\nEvaluation Scores\n")

    for metric, value in scores.items():

        print(f"{metric}: {value}")