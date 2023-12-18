from pathlib import Path

import pytest
from check_decrypted_secret.__main__ import check_env, check_secret
from .check_decrypted_secret_data import *


@pytest.mark.parametrize(
    "data,is_valid",
    [
        pytest.param(ENV_VALID, True, id="valid_env"),
        pytest.param(ENV_INVALID, False, id="invalid_env"),
    ],
)
def test_check_env(data: str, is_valid: bool, tmp_path: Path):
    tmp_path /= "test.env"
    tmp_path.write_text(data)
    path = tmp_path.as_posix()
    assert check_env(path) == is_valid


@pytest.mark.parametrize(
    "data,is_valid",
    [
        pytest.param(DATA_VALID, True, id="valid_yaml_data"),
        pytest.param(DATA_INVALID, False, id="invalid_yaml_data"),
        pytest.param(STRINGDATA_VALID, True, id="valid_yaml_stringdata"),
        pytest.param(STRINGDATA_INVALID, False, id="invalid_yaml_stringdata"),
    ],
)
def test_check_secret(data: str, is_valid: bool, tmp_path: Path):
    tmp_path /= "test.yaml"
    tmp_path.write_text(data)
    path = tmp_path.as_posix()
    assert check_secret(path) == is_valid
