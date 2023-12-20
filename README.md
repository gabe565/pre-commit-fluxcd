# Pre-Commit Hooks for FluxCD

A collection of [Pre-Commit](https://pre-commit.com) hooks for FluxCD GitOps repos.

## Installation

Add the following snippet to `.pre-commit-config.yaml`.

```yaml
hooks:
  - repo: https://github.com/gabe565/pre-commit-gitops
    rev: v0.2.0
    hooks:
      - id: check-charts-pinned
      - id: check-charts-support-renovate
      - id: check-secrets-encrypted
```

## Hooks

### `check-charts-pinned`
This hook ensures `HelmRelease` Kubernetes manifests have a version pinned at `.spec.chart.spec.version`.

### `check-charts-support-renovate`
[Renovate](https://docs.renovatebot.com/) will only update `HelmRelease` versions if [the following conditions are satisfied](https://docs.renovatebot.com/modules/manager/flux/#helmrelease-support):
- The `HelmRelease` resource has `metadata.namespace` or `spec.chart.spec.sourceRef.namespace` set
- The referenced `HelmRepository` has `metadata.namespace` set.

This hook ensures these conditions are satisfied.

### `check-secrets-encrypted`
This hook ensures `.env` files, and `Secret` Kubernetes manifests are encrypted using [SOPS](https://github.com/getsops/sops).
