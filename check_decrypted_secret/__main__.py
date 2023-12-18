#!/usr/bin/env python3

import re
import yaml
from os.path import abspath
from lib.paths import *


def main():
    failed = False
    env_mac_key = re.compile("^sops_mac=")
    for path in argv_or_glob(glob_env):
        with open(path) as file:
            for line in file:
                if env_mac_key.search(line):
                    break
            else:
                print(f"Env file decrypted: {abspath(path)}")
                failed = True
    for path in argv_or_glob(glob_yaml):
        with open(path) as file:
            for doc in yaml.safe_load_all(file):
                if "kind" not in doc or doc["kind"] != "Secret":
                    continue
                if "stringData" not in doc and "data" not in doc:
                    continue
                if "sops" not in doc:
                    print(f"Secret file decrypted: {abspath(path)}")
                    failed = True
    if failed:
        exit(1)


if __name__ == "__main__":
    main()
