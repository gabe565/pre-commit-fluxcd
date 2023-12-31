#!/usr/bin/env python3
import argparse
import sys
import re
import yaml
from os.path import abspath

from src.lib.kubernetes import is_secret

env_mac_key = re.compile("^sops_mac=")


def check_env(path: str) -> bool:
    with open(path) as file:
        for line in file:
            if env_mac_key.search(line):
                return True
    print(f"Env file decrypted: {abspath(path)}")
    return False


def check_secret(path: str) -> bool:
    with open(path) as file:
        for doc in yaml.safe_load_all(file):
            if not is_secret(doc):
                continue
            if "stringData" not in doc and "data" not in doc:
                continue
            if "sops" not in doc:
                print(f"Secret file decrypted: {abspath(path)}")
                return False
    return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="*")
    args = parser.parse_args()

    success = True
    for path in args.files:
        if path.endswith(".env"):
            success = check_env(path) and success
        elif path.endswith(".yaml") or path.endswith(".yml"):
            success = check_secret(path) and success
        else:
            print(f"Unknown file type: {abspath(path)}")
            success = False
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
