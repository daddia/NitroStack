# tests/utilities/test_vault_integration.py

import pytest
from unittest.mock import patch
from src.utilities.secrets.vault_integration import get_secret

@patch("src.utilities.secrets.vault_integration.client.is_authenticated", return_value=True)
@patch("src.utilities.secrets.vault_integration.client.secrets.kv.read_secret_version")
def test_get_secret(mock_read_secret, mock_auth):
    mock_read_secret.return_value = {"data": {"data": {"key": "value"}}}
    secret = get_secret("test/secret")
    assert secret["key"] == "value"
