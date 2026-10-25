from evaluate import evaluate
from data import DEV

TEMPLATE = (
    "Classify the sentiment of this review as positive or negative.\n"
    "Review: {review}\n"
    "Answer with one word."
)

accuracy, results = evaluate(TEMPLATE, DEV)

for i, r in enumerate(results):
    mark = "✓" if r["correct"] else "✗"
    print(f"{mark} [{i:2d}] true={r['label']:8s} pred={r['pred']:8s} raw={r['raw']!r}")
    if not r["correct"]:
        print(f"        review: {r['review']}")

print(f"\nAccuracy on DEV: {accuracy:.0%} ({sum(r['correct'] for r in results)}/{len(results)})")