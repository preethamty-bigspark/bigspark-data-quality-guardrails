def consistency_score(df, fields=[], threshold=0.95):
    inconsistencies = 0
    for field in fields:
        if field in df.columns:
            inconsistencies += df[field].duplicated().sum()
    total = len(df) * len(fields)
    score = 1 - (inconsistencies / total) if total else 0
    status = "pass" if score >= threshold else "fail"
    rating = 3 if score >= 0.98 else 2 if score >= 0.95 else 1
    return {
        "dimension": "consistency",
        "score": round(score, 4),
        "status": status,
        "rating": rating,
        "issues": [f"{inconsistencies} inconsistencies in {fields}"],
        "metadata": {"threshold": threshold, "checked_fields": fields}
    }