import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pre-commit-gitops",
    version="0.1.0",
    description="Pre-Commit hooks for GitOps repos",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gabe565/pre-commit-fluxcd",
    packages=setuptools.find_packages(),
    entry_points={
        "console_scripts": [
            "pre-commit-check-secrets-encrypted = check_secrets_encrypted.__main__:main",
            "pre-commit-check-charts-pinned = check_charts_pinned.__main__:main",
            "pre-commit-check-charts-support-renovate = check_charts_support_renovate.__main__:main",
        ]
    },
    install_requires=[
        "pyyaml==6.*",
    ],
    test_requires=[
        "pytest",
    ],
)
