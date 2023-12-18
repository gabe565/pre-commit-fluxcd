# Pre-Commit Hooks for FluxCD

A collection of [Pre-Commit](https://pre-commit.com) hooks for FluxCD GitOps repos.

## Installation

Add the following snippet to `.pre-commit-config.yaml`.

```yaml
hooks:
  - repo: https://github.com/gabe565/pre-commit-gitops
    rev: v0.0.1
    hooks:
      - id: check-decrypted-secret
      - id: check-unpinned-chart-version
```

## Hooks

### `check-decrypted-secret`

This hook ensures `.env` files, and that Kubernetes manifests with kind of `Secret` are encrypted using [SOPS](https://github.com/getsops/sops).

### `check-unpinned-chart-version`

This hook ensures Kubernetes manifests with kind of `HelmRelease` have a version pinned at `.spec.chart.spec.version`.
