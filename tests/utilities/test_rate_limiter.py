# tests/utilities/test_rate_limiter.py

import pytest
from unittest.mock import MagicMock, patch
from src.utilities.rate_limiter import rate_limiter

@patch("src.utilities.rate_limiter.redis.StrictRedis")
def test_rate_limiter(mock_redis):
    mock_client = MagicMock()
    mock_redis.return_value = mock_client
    mock_client.incr.return_value = 1

    try:
        rate_limiter("test_key", limit=3, window=10)
    except Exception:
        pytest.fail("Rate limiter should not raise an exception")

    mock_client.incr.return_value = 4
    with pytest.raises(Exception, match="Rate limit exceeded"):
        rate_limiter("test_key", limit=3, window=10)
