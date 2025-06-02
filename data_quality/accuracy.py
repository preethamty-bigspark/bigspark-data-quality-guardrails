def accuracy_score(df, reference_df=None, threshold=0.95):
    mismatches = (df != reference_df).sum().sum() if reference_df is not None else 0
    total = df.size
    score = 1 - (mismatches / total) if total else 0
    status = "pass" if score >= threshold else "fail"
    rating = 3 if score >= 0.98 else 2 if score >= 0.95 else 1
    return {
        "dimension": "accuracy",
        "score": round(score, 4),
        "status": status,
        "rating": rating,
        "issues": [f"{mismatches} mismatched cells"] if mismatches else [],
        "metadata": {"threshold": threshold, "total_cells": total, "mismatches": mismatches}
    }