from llm import chat


def normalize(answer):
    """Turn the model's messy text into 'positive', 'negative' or 'unknown'."""
    a = answer.lower()
    has_pos = "positive" in a
    has_neg = "negative" in a
    if has_pos and not has_neg:
        return "positive"
    if has_neg and not has_pos:
        return "negative"
    return "unknown"


def evaluate(template, data):
    """Run a prompt template on every (review, label) pair.
    Returns accuracy and a list of per-review results."""
    results = []
    correct = 0
    for review, label in data:
        prompt = template.format(review=review)
        raw = chat(prompt)
        pred = normalize(raw)
        is_correct = pred == label
        correct += is_correct
        results.append(
            {"review": review, "label": label, "raw": raw, "pred": pred, "correct": is_correct}
        )
    return correct / len(data), results