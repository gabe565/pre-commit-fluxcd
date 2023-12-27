#!/usr/bin/env python3
import argparse
import sys
import yaml
from os.path import abspath

from src.lib.kubernetes import is_helm_release


def check_helm_release(path: str) -> bool:
    with open(path) as file:
        try:
            for doc in yaml.safe_load_all(file):
                if not is_helm_release(doc):
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
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="*")
    args = parser.parse_args()

    success = True
    for path in args.files:
        if path.endswith(".yaml") or path.endswith(".yml"):
            success = check_helm_release(path) and success
        else:
            print(f"Unknown file type: {abspath(path)}")
            success = False
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
