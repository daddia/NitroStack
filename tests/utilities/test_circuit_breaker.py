# tests/utilities/test_circuit_breaker.py

import pytest
from src.utilities.resilience.circuit_breaker import with_circuit_breaker, CircuitBreakerError

def failing_function():
    raise ValueError("Intentional failure")

@with_circuit_breaker
def flaky_service():
    return failing_function()

def test_circuit_breaker():
    for _ in range(5):
        with pytest.raises(ValueError):
            flaky_service()

    with pytest.raises(CircuitBreakerError):
        flaky_service()
