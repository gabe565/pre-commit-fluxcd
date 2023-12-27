from pathlib import Path

import pytest
from src.check_drift_detection_enabled.__main__ import check_helm_release
from .data import HELM_RELEASE_ENABLED, HELM_RELEASE_WARN, HELM_RELEASE_MISSING


@pytest.mark.parametrize(
    "data,allow_warn,is_valid",
    [
        pytest.param(
            HELM_RELEASE_ENABLED, False, True, id="helm_release_drift_enabled"
        ),
        pytest.param(
            HELM_RELEASE_WARN, False, False, id="helm_release_drift_warn_failed"
        ),
        pytest.param(
            HELM_RELEASE_WARN, True, True, id="helm_release_drift_warn_passed"
        ),
        pytest.param(
            HELM_RELEASE_MISSING, False, False, id="helm_release_drift_missing"
        ),
    ],
)
def test_check_helm_release(
    data: str, allow_warn: bool, is_valid: bool, tmp_path: Path
):
    tmp_path /= "test.yaml"
    tmp_path.write_text(data)
    path = tmp_path.as_posix()
    assert check_helm_release(path, allow_warn) == is_valid
