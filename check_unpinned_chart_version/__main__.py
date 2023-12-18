#!/usr/bin/env python3

import yaml
from os.path import abspath
from lib.paths import *


def main():
    failed = False
    for path in argv_or_glob(glob_yaml):
        with open(path) as file:
            try:
                for doc in yaml.safe_load_all(file):
                    if "kind" not in doc or doc["kind"] != "HelmRelease":
                        continue
                    if "version" not in doc["spec"]["chart"]["spec"]:
                        print(f"HelmRelease missing version: {abspath(path)}")
                        failed = True
            except Exception as err:
                print(f"HelmRelease malformed: {abspath(path)}")
                print(err)
                failed = True
    if failed:
        exit(1)


if __name__ == "__main__":
    main()
