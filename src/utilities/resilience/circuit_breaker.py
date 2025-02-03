from pybreaker import CircuitBreaker, CircuitBreakerError
import logging

logger = logging.getLogger(__name__)

# Basic Circuit Breaker Configuration
circuit_breaker = CircuitBreaker(fail_max=5, reset_timeout=60)

def with_circuit_breaker(func):
    def wrapper(*args, **kwargs):
        try:
            return circuit_breaker.call(func, *args, **kwargs)
        except CircuitBreakerError:
            logger.error(f"Circuit breaker is OPEN for {func.__name__}")
            raise
    return wrapper