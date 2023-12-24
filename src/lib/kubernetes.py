def is_secret(data):
    try:
        return data["apiVersion"] == "v1" and data["kind"] == "Secret"
    except (KeyError, TypeError):
        return False


def is_helm_release(data):
    try:
        return (
            data["apiVersion"].startswith("helm.toolkit.fluxcd.io/")
            and data["kind"] == "HelmRelease"
        )
    except (KeyError, TypeError):
        return False


def is_helm_repository(data):
    try:
        return (
            data["apiVersion"].startswith("source.toolkit.fluxcd.io/")
            and data["kind"] == "HelmRepository"
        )
    except (KeyError, TypeError):
        return False
