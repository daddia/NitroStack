import pytest
from unittest.mock import MagicMock
from utilities.rate_limiter import rate_limiter

def test_rate_limiter():
    # Mock Redis client
    mock_redis_client = MagicMock()
    
    # Mock the 'incr' and 'expire' methods
    mock_redis_client.incr.return_value = 1
    mock_redis_client.expire.return_value = True

    # Test when the rate limit has NOT been exceeded
    try:
        rate_limiter("test_key", limit=3, window=10, redis_client=mock_redis_client)
    except Exception:
        pytest.fail("Rate limiter should not raise an exception")

    # Simulate exceeding the rate limit
    mock_redis_client.incr.return_value = 4  # Simulate hitting the limit
    with pytest.raises(Exception, match="Rate limit exceeded"):
        rate_limiter("test_key", limit=3, window=10, redis_client=mock_redis_client)
