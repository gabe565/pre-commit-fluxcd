from pathlib import Path

import pytest
from check_unpinned_chart_version.__main__ import check_helm_release
from .check_unpinned_chart_version_data import HELM_RELEASE_VALID, HELM_RELEASE_INVALID


@pytest.mark.parametrize(
    "data,is_valid",
    [
        pytest.param(HELM_RELEASE_VALID, True, id="valid_helm_release"),
        pytest.param(HELM_RELEASE_INVALID, False, id="invalid_helm_release"),
    ],
)
def test_check_helm_release(data: str, is_valid: bool, tmp_path: Path):
    tmp_path /= "test.yaml"
    tmp_path.write_text(data)
    path = tmp_path.as_posix()
    assert check_helm_release(path) == is_valid
