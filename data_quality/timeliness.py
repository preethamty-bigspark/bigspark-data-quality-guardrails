from datetime import datetime, timedelta
import pandas as pd

def timeliness_score(df, date_col, max_days_lag=2):
    now = datetime.utcnow()
    df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
    outdated = (now - df[date_col]).dt.days > max_days_lag
    count_outdated = outdated.sum()
    score = 1 - (count_outdated / len(df)) if len(df) else 0
    status = "pass" if score >= 0.95 else "fail"
    rating = 3 if score >= 0.98 else 2 if score >= 0.95 else 1
    return {
        "dimension": "timeliness",
        "score": round(score, 4),
        "status": status,
        "rating": rating,
        "issues": [f"{count_outdated} records are older than {max_days_lag} days"],
        "metadata": {"threshold_days": max_days_lag}
    }