# tests/utilities/test_retry.py

import pytest
from src.utilities.resilience.retry import retry_on_failure

@retry_on_failure(max_attempts=3)
def flaky_function():
    raise ValueError("Retry error")

def test_retry_success():
    with pytest.raises(ValueError):
        flaky_function()
