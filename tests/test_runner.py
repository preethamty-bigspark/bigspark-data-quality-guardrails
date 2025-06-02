import pandas as pd
import json
import yaml
import os
from data_quality.dq_runner import run_all_dq_tests

# ──────────────────────────────────────────────
# 1. Load Input Dataset
# ──────────────────────────────────────────────
data_path = "data/input_data.csv"
df = pd.read_csv(data_path)

# ──────────────────────────────────────────────
# 2. Load Thresholds and Schema Config
# ──────────────────────────────────────────────
config_path = "configs/thresholds.yaml"
with open(config_path, "r") as f:
    config = yaml.safe_load(f)

# ──────────────────────────────────────────────
# 3. Run All Data Quality Tests
# ──────────────────────────────────────────────
results = run_all_dq_tests(df, config)

# ──────────────────────────────────────────────
# 4. Print to Console
# ──────────────────────────────────────────────
print("\n🔍 Bigspark Data Quality Guardrail Results:\n")
for result in results:
    print(f"🔸 {result['dimension'].capitalize()} Test")
    print(f"    Score : {result['score']}")
    print(f"    Status: {result['status']}")
    print(f"    Rating: {result['rating']}")
    print(f"    Issues: {result['issues']}\n")

# ──────────────────────────────────────────────
# 5. Save JSON Report
# ──────────────────────────────────────────────
os.makedirs("reports", exist_ok=True)
with open("reports/dq_report.json", "w") as f:
    json.dump(results, f, indent=4)

print("✅ JSON report saved to reports/dq_report.json")