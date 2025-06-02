def completeness_score(df, threshold=0.95):
    nulls = df.isnull().sum().sum()
    total = df.size
    score = 1 - (nulls / total) if total else 0
    status = "pass" if score >= threshold else "fail"
    rating = 3 if score >= 0.98 else 2 if score >= 0.95 else 1
    return {
        "dimension": "completeness",
        "score": round(score, 4),
        "status": status,
        "rating": rating,
        "issues": [f"{nulls} missing values"] if nulls else [],
        "metadata": {"threshold": threshold, "total_cells": total, "nulls": nulls}
    }