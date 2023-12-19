#!/usr/bin/env python3

import sys
import yaml
from os.path import abspath
from lib.paths import argv_or_glob, glob_yaml


def check_helm_release(path: str) -> bool:
    with open(path) as file:
        for doc in yaml.safe_load_all(file):
            if "kind" not in doc or doc["kind"] != "HelmRelease":
                continue
            if "namespace" in doc["metadata"]:
                continue
            try:
                if doc["spec"]["chart"]["spec"]["sourceRef"]["namespace"]:
                    continue
            except KeyError:
                pass
            print(
                f"HelmRelease missing metadata.namespace and spec.chart.spec.sourceRef.namespace: {abspath(path)}"
            )
            return False
    return True


def check_helm_repository(path: str) -> bool:
    with open(path) as file:
        for doc in yaml.safe_load_all(file):
            if "kind" not in doc or doc["kind"] != "HelmRepository":
                continue
            if "namespace" in doc["metadata"]:
                continue
            print(f"HelmRepository missing metadata.namespace: {abspath(path)}")
            return False
    return True


def main():
    success = True
    for path in argv_or_glob(glob_yaml):
        success = check_helm_release(path) and check_helm_repository(path) and success
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
