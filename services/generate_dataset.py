import random
import pandas as pd
import os

os.makedirs("data", exist_ok=True)

issues = [
    "refund",
    "late delivery",
    "wrong product",
    "damaged item",
    "password reset",
    "subscription cancellation",
    "payment failed",
    "double charged",
    "tracking request",
    "change address"
]

templates = {
    "refund": (
        "I haven't received my refund.",
        "We're sorry for the delay. Your refund is being processed and should arrive within 3-5 business days."
    ),
    "late delivery": (
        "My order is late.",
        "We apologize for the delay. Your package is in transit and should arrive soon."
    ),
    "wrong product": (
        "I received the wrong product.",
        "We're sorry for the mistake. We'll ship the correct item immediately."
    ),
    "damaged item": (
        "My item arrived damaged.",
        "We're extremely sorry. We'll replace your damaged product immediately."
    ),
    "password reset": (
        "I forgot my password.",
        "Please click on 'Forgot Password' to reset your password."
    ),
    "subscription cancellation": (
        "Cancel my subscription.",
        "Your subscription has been cancelled successfully."
    ),
    "payment failed": (
        "Payment is failing.",
        "Please try another payment method or contact your bank."
    ),
    "double charged": (
        "I was charged twice.",
        "We'll investigate the duplicate payment and issue a refund if applicable."
    ),
    "tracking request": (
        "Where is my order?",
        "You can track your shipment using the tracking link sent via email."
    ),
    "change address": (
        "I need to change my delivery address.",
        "If the order hasn't shipped yet, we'll update your address."
    )
}

rows = []

for _ in range(250):

    issue = random.choice(issues)

    email, response = templates[issue]

    rows.append(
        {
            "customer_email": email,
            "human_response": response
        }
    )

df = pd.DataFrame(rows)

df.to_csv("data/emails.csv", index=False)

print("Dataset Generated Successfully")

print("Rows:", len(df))