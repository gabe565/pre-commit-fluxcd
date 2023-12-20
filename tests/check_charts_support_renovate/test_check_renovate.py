from pathlib import Path

import pytest
from check_charts_support_renovate.__main__ import (
    check_helm_release,
    check_helm_repository,
)
from .data import (
    HELM_RELEASE_METADATA_VALID,
    HELM_RELEASE_SOURCE_REF_VALID,
    HELM_RELEASE_INVALID,
    HELM_REPOSITORY_VALID,
    HELM_REPOSITORY_INVALID,
)


@pytest.mark.parametrize(
    "data,is_valid",
    [
        pytest.param(
            HELM_RELEASE_METADATA_VALID, True, id="valid_helm_release_metadata"
        ),
        pytest.param(
            HELM_RELEASE_SOURCE_REF_VALID, True, id="valid_helm_release_source_ref"
        ),
        pytest.param(HELM_RELEASE_INVALID, False, id="invalid_helm_release"),
    ],
)
def test_check_helm_release(data: str, is_valid: bool, tmp_path: Path):
    tmp_path /= "test.yaml"
    tmp_path.write_text(data)
    path = tmp_path.as_posix()
    assert check_helm_release(path) == is_valid


@pytest.mark.parametrize(
    "data,is_valid",
    [
        pytest.param(HELM_REPOSITORY_VALID, True, id="invalid_helm_repository"),
        pytest.param(HELM_REPOSITORY_INVALID, False, id="invalid_helm_repository"),
    ],
)
def test_check_helm_repository(data: str, is_valid: bool, tmp_path: Path):
    tmp_path /= "test.yaml"
    tmp_path.write_text(data)
    path = tmp_path.as_posix()
    assert check_helm_repository(path) == is_valid
