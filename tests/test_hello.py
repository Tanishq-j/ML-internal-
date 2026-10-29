"""
Unit tests for hello.py application
"""
import pytest
from hello import get_message, predict_score

def test_hello_default():
    """Verify default greeting message."""
    expected = "Hello, World!"
    actual = get_message()
    assert actual == expected, f"Expected '{expected}' but got '{actual}'"

def test_hello_custom_name():
    """Verify custom name greeting."""
    assert get_message("DevOps") == "Hello, DevOps!"

def test_predict_score():
    """Verify ML inference / score calculation."""
    assert predict_score(2.0) == 5.0
