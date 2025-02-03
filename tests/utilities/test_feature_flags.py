# tests/utilities/test_feature_flags.py

import pytest
from unittest.mock import patch
from src.utilities.feature_flags import is_feature_enabled

@patch("src.utilities.feature_flags.requests.get")
def test_is_feature_enabled(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"enabled": True}

    assert is_feature_enabled("new_feature") is True

    mock_get.return_value.json.return_value = {"enabled": False}
    assert is_feature_enabled("old_feature") is False
