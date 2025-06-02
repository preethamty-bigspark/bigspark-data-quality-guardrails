def uniqueness_score(df, id_col, threshold=0.99):
    duplicate_count = df.duplicated(subset=[id_col]).sum()
    total = len(df)
    score = 1 - (duplicate_count / total) if total else 0
    status = "pass" if score >= threshold else "fail"
    rating = 3 if score >= 0.995 else 2 if score >= 0.99 else 1
    return {
        "dimension": "uniqueness",
        "score": round(score, 4),
        "status": status,
        "rating": rating,
        "issues": [f"{duplicate_count} duplicate {id_col} values"],
        "metadata": {"threshold": threshold, "duplicates": duplicate_count}
    }