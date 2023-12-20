def is_secret(data):
    try:
        return data["apiVersion"] == "v1" and data["kind"] == "Secret"
    except KeyError:
        return False


def is_helm_release(data):
    try:
        return (
            data["apiVersion"].startswith("helm.toolkit.fluxcd.io/")
            and data["kind"] == "HelmRelease"
        )
    except KeyError:
        return False


def is_helm_repository(data):
    try:
        return (
            data["apiVersion"].startswith("source.toolkit.fluxcd.io/")
            and data["kind"] == "HelmRepository"
        )
    except KeyError:
        return False
