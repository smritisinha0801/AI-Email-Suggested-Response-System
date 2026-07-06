from services.generator import EmailGenerator


def main():

    print("=" * 70)
    print("AI EMAIL SUGGESTED RESPONSE SYSTEM")
    print("=" * 70)

    generator = EmailGenerator()

    while True:

        customer_email = input(
            "\nEnter Customer Email (or type 'exit' to quit):\n\n"
        )

        if customer_email.lower() == "exit":
            print("\nThank you!")
            break

        reply, retrieved, scores = generator.generate_reply(customer_email)

        print("\n")
        print("=" * 70)
        print("AI SUGGESTED RESPONSE")
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
        print("EVALUATION METRICS")
        print("=" * 70)

        for metric, value in scores.items():
            print(f"{metric}: {value}")

        # Overall System Score
        overall_score = (
            scores["BLEU"] +
            scores["ROUGE-L"] +
            scores["Cosine Similarity"]
        ) / 3

        print("\n")
        print("=" * 70)
        print("OVERALL SYSTEM SCORE")
        print("=" * 70)
        print(f"Overall Quality Score: {overall_score:.4f}")
        print("=" * 70)


if __name__ == "__main__":
    main()