#!/usr/bin/env python3

import yaml
from os.path import abspath
from lib.paths import *


def check_helm_release(path: str) -> bool:
    with open(path) as file:
        try:
            for doc in yaml.safe_load_all(file):
                if "kind" not in doc or doc["kind"] != "HelmRelease":
                    continue
                if "version" not in doc["spec"]["chart"]["spec"]:
                    print(f"HelmRelease missing version: {abspath(path)}")
                    return False
        except Exception as err:
            print(f"HelmRelease malformed: {abspath(path)}")
            print(err)
            return False
    return True


def main():
    success = True
    for path in argv_or_glob(glob_yaml):
        success = check_helm_release(path) and success
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
