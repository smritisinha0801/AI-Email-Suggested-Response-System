SYSTEM_PROMPT = """
You are an AI Customer Support Agent.

Your job is to generate professional email replies.

Rules:

1. Be polite.
2. Be empathetic.
3. Keep replies under 120 words.
4. Never invent policies.
5. Use the retrieved reference responses only as guidance.
6. If the customer's name is unknown, don't use a name.
7. End every reply with:

Best Regards,
Support Team
"""


def build_prompt(customer_email, retrieved_examples):
    """
    Builds the prompt sent to the LLM.
    """

    prompt = f"""
Customer Email:
{customer_email}

Below are similar customer issues and their ideal responses.

"""

    for i, example in enumerate(retrieved_examples, start=1):

        prompt += f"""
Example {i}

Customer:
{example["customer_email"]}

Response:
{example["human_response"]}

"""

    prompt += """

Generate ONE professional customer support email.

Requirements:

- Don't copy the examples word-for-word.
- Write naturally.
- Be empathetic.
- Keep the response concise.
- Output ONLY the email response.
"""

    return prompt

if __name__ == "__main__":

    sample_examples = [
        {
            "customer_email": "I haven't received my refund.",
            "human_response": "We're sorry for the delay. Your refund will be processed within 3-5 business days."
        },
        {
            "customer_email": "My order is late.",
            "human_response": "We apologize for the delay. Your package is on the way."
        }
    ]

    prompt = build_prompt(
        "My refund is taking too long.",
        sample_examples
    )

    print(prompt)