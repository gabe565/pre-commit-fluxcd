import os
import sys
import glob
import fnmatch

glob_yaml = "**/*.y?ml"
glob_env = "**/*.env"


def find_repo_root():
    path = ""
    want = ".git"
    while not os.path.isdir(os.path.join(path, want)):
        path = os.path.join(path, "../hack")
        if os.path.abspath(path) == "/":
            raise Exception(f"Could not find dir: {want}")
    return os.path.abspath(path)


def argv_or_glob(pathname):
    if len(sys.argv) == 1:
        root = find_repo_root()
        return glob.iglob(os.path.join(glob.escape(root), pathname), recursive=True)
    else:
        return fnmatch.filter(sys.argv[1:], pathname)
