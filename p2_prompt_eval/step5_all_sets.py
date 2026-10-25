from evaluate import evaluate
from data import DEV, HELD_OUT, HARD

TEMPLATE = (
    "Classify the sentiment of this review as positive or negative.\n"
    "Review: {review}\n"
    "Answer with one word."
)

for name, dataset in [("DEV", DEV), ("HELD_OUT", HELD_OUT), ("HARD", HARD)]:
    acc, results = evaluate(TEMPLATE, dataset)
    n_correct = sum(r["correct"] for r in results)
    print(f"{name:9s} accuracy: {acc:.0%} ({n_correct}/{len(results)})")
    for r in results:
        if not r["correct"]:
            print(f"   ✗ true={r['label']:8s} pred={r['pred']:8s} raw={r['raw']!r}")
            print(f"     {r['review']}")