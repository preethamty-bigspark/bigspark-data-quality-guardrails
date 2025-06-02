def validity_score(df, schema_dict):
    invalids = 0
    for col, expected_type in schema_dict.items():
        if col in df.columns:
            invalid_col = ~df[col].apply(lambda x: isinstance(x, expected_type))
            invalids += invalid_col.sum()
    total = len(df) * len(schema_dict)
    score = 1 - (invalids / total) if total else 0
    status = "pass" if score >= 0.95 else "fail"
    rating = 3 if score >= 0.98 else 2 if score >= 0.95 else 1
    return {
        "dimension": "validity",
        "score": round(score, 4),
        "status": status,
        "rating": rating,
        "issues": [f"{invalids} invalid type entries"] if invalids > 0 else [],
        "metadata": {"tested_fields": list(schema_dict.keys())}
    }