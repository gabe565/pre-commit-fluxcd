#!/usr/bin/env python3
import argparse
import sys
import yaml
from os.path import abspath

from src.lib.kubernetes import is_helm_release


def check_helm_release(path: str, allow_warn: bool) -> bool:
    with open(path) as file:
        try:
            for doc in yaml.safe_load_all(file):
                if not is_helm_release(doc):
                    continue
                try:
                    mode = doc["spec"]["driftDetection"]["mode"]
                    if mode == "enabled":
                        continue
                    if mode == "warn":
                        if allow_warn:
                            return True
                        print(
                            f"HelmRelease drift detection warn not allowed: {abspath(path)}"
                        )
                    return False
                except KeyError:
                    print(f"HelmRelease drift detection disabled: {abspath(path)}")
                    return False
        except Exception as err:
            print(f"HelmRelease malformed: {abspath(path)}")
            print(err)
            return False
    return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="*")
    parser.add_argument(
        "--allow-warn", action=argparse.BooleanOptionalAction, default=False
    )
    args = parser.parse_args()

    success = True
    for path in args.files:
        if path.endswith(".yaml") or path.endswith(".yml"):
            success = check_helm_release(path, args.allow_warn) and success
        else:
            print(f"Unknown file type: {abspath(path)}")
            success = False
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
