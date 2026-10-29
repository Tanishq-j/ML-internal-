"""
evidently_monitor.py - MLOps Monitoring Script using Evidently AI
Monitors data drift and data quality between reference (training) and current (UAT) datasets.
"""
import json
import numpy as np
import pandas as pd
from hello import predict_score

def generate_mock_datasets(n_reference=200, n_current=100):
    """
    Generate synthetic reference and current inference data for UAT dry run.
    """
    np.random.seed(42)
    # Reference baseline data
    ref_feature = np.random.normal(loc=5.0, scale=1.0, size=n_reference)
    ref_scores = [predict_score(x) for x in ref_feature]
    reference_df = pd.DataFrame({
        "feature_input": ref_feature,
        "prediction_score": ref_scores,
    })

    # Current UAT production data (simulated with slight drift)
    cur_feature = np.random.normal(loc=5.5, scale=1.2, size=n_current)
    cur_scores = [predict_score(x) for x in cur_feature]
    current_df = pd.DataFrame({
        "feature_input": cur_feature,
        "prediction_score": cur_scores,
    })

    return reference_df, current_df

def run_monitoring():
    print("=" * 65)
    print("      Evidently AI - Model & Data Drift Monitoring (UAT)")
    print("=" * 65)
    
    ref_data, curr_data = generate_mock_datasets()
    print(f"[INFO] Generated Reference Baseline: {ref_data.shape[0]} rows")
    print(f"[INFO] Generated Current UAT Sample: {curr_data.shape[0]} rows")

    try:
        from evidently import Report
        from evidently.presets import DataDriftPreset, DataSummaryPreset

        print("[INFO] Initializing Evidently Report with DataDriftPreset & DataSummaryPreset...")
        report = Report(metrics=[
            DataDriftPreset(),
            DataSummaryPreset()
        ])

        print("[INFO] Computing dataset drift and statistical metrics...")
        snapshot = report.run(reference_data=ref_data, current_data=curr_data)

        # Save HTML visual report
        html_output = "evidently_report.html"
        snapshot.save_html(html_output)
        print(f"[SUCCESS] Visual HTML report generated: {html_output}")

        # Save JSON metrics summary
        json_output = "evidently_metrics.json"
        snapshot.save_json(json_output)
        print(f"[SUCCESS] Metrics summary saved to: {json_output}")

        print("-" * 65)
        print("UAT MONITORING DRY RUN RESULT: SUCCESS")
        print("  - Drift and Data Quality presets evaluated successfully.")
        print(f"  - Baseline Mean Score: {ref_data['prediction_score'].mean():.2f}")
        print(f"  - Current UAT Mean Score: {curr_data['prediction_score'].mean():.2f}")
        print("-" * 65)
        return True

    except Exception as e:
        print(f"[ERROR] Evidently execution error: {e}")
        # Statistical fallback summary
        summary = {
            "ref_mean_score": float(ref_data["prediction_score"].mean()),
            "curr_mean_score": float(curr_data["prediction_score"].mean()),
            "status": "Evidently fallback summary active"
        }
        with open("evidently_metrics.json", "w") as f:
            json.dump(summary, f, indent=2)
        print("[INFO] Fallback metrics written to evidently_metrics.json")
        return False

if __name__ == "__main__":
    run_monitoring()
