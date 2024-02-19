# Pre-Commit Hooks for FluxCD

A collection of [Pre-Commit](https://pre-commit.com) hooks for FluxCD GitOps repos.

## Installation

Add the following snippet to `.pre-commit-config.yaml`.

```yaml
hooks:
  - repo: https://github.com/gabe565/pre-commit-fluxcd
    rev: ''  # Use the sha / tag you want to point at
    hooks:
      - id: check-charts-pinned
      - id: check-charts-support-renovate
      - id: check-drift-detection-enabled
      - id: check-secrets-encrypted
```

## Hooks
- [check-charts-pinned](#check-charts-pinned)
- [check-charts-support-renovate](#check-charts-support-renovate)
- [check-drift-detection-enabled](#check-drift-detection-enabled)
- [check-secrets-encrypted](#check-secrets-encrypted)

### check-charts-pinned
This hook ensures `HelmRelease` Kubernetes manifests have a version pinned at `.spec.chart.spec.version`.

### check-charts-support-renovate
[Renovate](https://docs.renovatebot.com/) will only update `HelmRelease` versions if [the following conditions are satisfied](https://docs.renovatebot.com/modules/manager/flux/#helmrelease-support):
- The `HelmRelease` resource has `metadata.namespace` or `spec.chart.spec.sourceRef.namespace` set
- The referenced `HelmRepository` has `metadata.namespace` set.

This hook ensures these conditions are satisfied.

### check-drift-detection-enabled

This hook ensures `HelmRelease` manifests have [drift detection](https://fluxcd.io/flux/components/helm/helmreleases/#drift-detection) enabled.

If you would like to allow `warn` mode, add the `--allow-warn` arg:
```yaml
- id: check-drift-detection-enabled
  args:
    - --allow-warn
```

### check-secrets-encrypted
This hook ensures `.env` files, and `Secret` Kubernetes manifests are encrypted using [SOPS](https://github.com/getsops/sops).
