# tests/utilities/test_circuit_breaker.py

import pytest
from src.utilities.resilience.circuit_breaker import with_circuit_breaker, CircuitBreakerError

def failing_function():
    raise ValueError("Intentional failure")

@with_circuit_breaker
def flaky_service():
    return failing_function()

def test_circuit_breaker():
    # Trigger failures up to the threshold
    for _ in range(4):  # Trigger 4 failures (threshold is 5)
        with pytest.raises(ValueError):
            flaky_service()

    # The 5th failure should open the circuit
    with pytest.raises(CircuitBreakerError):
        flaky_service()
