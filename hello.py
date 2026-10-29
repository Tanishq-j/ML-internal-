"""
hello.py - Very simple single-file application for MLOps UAT Environment.
Contains basic greetings and a data scoring function for testing & monitoring.
"""
import sys

def get_message(name: str = "World") -> str:
    """Return greeting message."""
    return f"Hello, {name}!"

def predict_score(feature_val: float) -> float:
    """
    Simulate a lightweight ML inference / score calculation.
    Formula: score = feature_val * 1.5 + 2.0
    """
    return round(float(feature_val) * 1.5 + 2.0, 2)

def main():
    name = sys.argv[1] if len(sys.argv) > 1 else "World"
    print(get_message(name))
    test_feature = 3.5
    print(f"Sample prediction for feature={test_feature}: {predict_score(test_feature)}")

if __name__ == "__main__":
    main()
