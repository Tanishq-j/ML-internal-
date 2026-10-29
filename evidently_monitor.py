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
    # Reference data (normal baseline)
    ref_feature = np.random.normal(loc=5.0, scale=1.0, size=n_reference)
    ref_scores = [predict_score(x) for x in ref_feature]
    reference_df = pd.DataFrame({
        "feature_input": ref_feature,
        "prediction_score": ref_scores,
    })

    # Current UAT data (with slight drift to verify monitoring capabilities)
    cur_feature = np.random.normal(loc=5.3, scale=1.2, size=n_current)
    cur_scores = [predict_score(x) for x in cur_feature]
    current_df = pd.DataFrame({
        "feature_input": cur_feature,
        "prediction_score": cur_scores,
    })

    return reference_df, current_df

def run_monitoring():
    print("=" * 60)
    print("      Evidently AI - Model & Data Drift Monitoring")
    print("=" * 60)
    
    ref_data, curr_data = generate_mock_datasets()
    print(f"[INFO] Generated Reference Dataset: {ref_data.shape[0]} records")
    print(f"[INFO] Generated Current (UAT) Dataset: {curr_data.shape[0]} records")

    try:
        from evidently.report import Report
        from evidently.metric_preset import DataDriftPreset, DataQualityPreset

        # Initialize Report with Data Drift and Quality presets
        report = Report(metrics=[
            DataDriftPreset(),
            DataQualityPreset()
        ])

        print("[INFO] Running Evidently drift calculation...")
        report.run(reference_data=ref_data, current_data=curr_data)

        # Save HTML visual report
        html_output = "evidently_report.html"
        report.save_html(html_output)
        print(f"[SUCCESS] Evidently HTML report generated: {html_output}")

        # Save JSON metrics summary
        json_output = "evidently_metrics.json"
        report.save_json(json_output)
        print(f"[SUCCESS] Evidently JSON metrics generated: {json_output}")

        # Extract and print high-level drift summary
        metrics_dict = report.as_dict()
        drift_metrics = metrics_dict.get("metrics", [{}])[0].get("result", {})
        drift_share = drift_metrics.get("share_of_drifted_columns", "N/A")
        dataset_drift = drift_metrics.get("dataset_drift", "N/A")

        print("-" * 60)
        print("MONITORING SUMMARY:")
        print(f"  Dataset Drift Detected : {dataset_drift}")
        print(f"  Drifted Columns Share  : {drift_share}")
        print("-" * 60)
        return True

    except Exception as e:
        print(f"[WARNING] Could not run full Evidently presets ({e}). Falling back to statistical summary.")
        # Lightweight statistical fallback if dependency issues arise
        summary = {
            "ref_mean_score": float(ref_data["prediction_score"].mean()),
            "curr_mean_score": float(curr_data["prediction_score"].mean()),
            "status": "Monitored via baseline statistical tracking"
        }
        with open("evidently_metrics.json", "w") as f:
            json.dump(summary, f, indent=2)
        print(f"[INFO] Fallback metrics written to evidently_metrics.json")
        return False

if __name__ == "__main__":
    run_monitoring()
