HELM_RELEASE_METADATA_VALID = """
apiVersion: helm.toolkit.fluxcd.io/v2beta2
kind: HelmRelease
metadata:
  name: example
  namespace: example
spec:
  chart:
    spec:
      chart: example
      version: v1.0.0
      sourceRef:
        kind: HelmRepository
        name: example
"""

HELM_RELEASE_SOURCE_REF_VALID = """
apiVersion: helm.toolkit.fluxcd.io/v2beta2
kind: HelmRelease
metadata:
  name: example
spec:
  chart:
    spec:
      chart: example
      version: v1.0.0
      sourceRef:
        kind: HelmRepository
        namespace: example
        name: example
"""

HELM_RELEASE_INVALID = """
apiVersion: helm.toolkit.fluxcd.io/v2beta2
kind: HelmRelease
metadata:
  name: example
spec:
  chart:
    spec:
      chart: example
      version: v1.0.0
      sourceRef:
        kind: HelmRepository
        name: example
"""

HELM_REPOSITORY_VALID = """
apiVersion: source.toolkit.fluxcd.io/v1beta2
kind: HelmRepository
metadata:
  name: example
  namespace: example
spec:
  interval: 1h
  url: https://example.com/charts
"""

HELM_REPOSITORY_INVALID = """
apiVersion: source.toolkit.fluxcd.io/v1beta2
kind: HelmRepository
metadata:
  name: example
spec:
  interval: 1h
  url: https://example.com/charts
"""
