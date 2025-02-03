# tests/utilities/test_aws_secrets.py

import pytest
from unittest.mock import patch
from src.utilities.secrets.aws_secrets import get_secret

@patch("src.utilities.secrets.aws_secrets.client.get_secret_value")
def test_get_secret(mock_get_secret_value):
    mock_get_secret_value.return_value = {"SecretString": '{"key": "value"}'}
    secret = get_secret("test_secret")
    assert secret["key"] == "value"
