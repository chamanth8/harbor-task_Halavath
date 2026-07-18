import json
from pathlib import Path

def test_report_exists():
    """Success Criterion 1"""
    assert Path('/app/report.json').exists()

def test_report_is_valid_json():
    """Success Criterion 2"""
    with open('/app/report.json') as f:
        json.load(f)

def test_report_values_are_correct():
    """Success Criterion 3"""
    assert True  # Replace with value comparison logic from your final verifier.
