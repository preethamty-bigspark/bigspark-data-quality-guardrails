from .accuracy import accuracy_score
from .completeness import completeness_score
from .consistency import consistency_score
from .timeliness import timeliness_score
from .uniqueness import uniqueness_score
from .validity import validity_score

def run_all_dq_tests(df, config, reference_df=None):
    results = []
    results.append(accuracy_score(df, reference_df, config.get("accuracy_threshold", 0.95)))
    results.append(completeness_score(df, config.get("completeness_threshold", 0.95)))
    results.append(consistency_score(df, config.get("consistency_fields", [])))
    results.append(uniqueness_score(df, config.get("id_col", "id")))
    results.append(validity_score(df, config.get("schema", {})))
    results.append(timeliness_score(df, config.get("date_col", "created_at")))
    return results