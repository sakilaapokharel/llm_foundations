from llm import chat
from data import DEV

TEMPLATE = (
    "Classify the sentiment of this review as positive or negative.\n"
    "Review: {review}\n"
    "Answer with one word."
)

review, true_label = DEV[0]

prompt = TEMPLATE.format(review=review)
print("PROMPT SENT:\n" + prompt + "\n")

answer = chat(prompt)
print("MODEL ANSWER:", repr(answer))
print("TRUE LABEL:  ", true_label)