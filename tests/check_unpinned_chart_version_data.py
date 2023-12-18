HELMRELEASE_VALID = """
apiVersion: helm.toolkit.fluxcd.io/v2beta2
kind: HelmRelease
metadata:
  name: example
spec:
  chart:
    spec:
      chart: example
      version: 1.0.0
      sourceRef:
        kind: HelmRepository
        namespace: flux-system
        name: example
"""

HELMRELEASE_INVALID = """
apiVersion: helm.toolkit.fluxcd.io/v2beta2
kind: HelmRelease
metadata:
  name: example
spec:
  chart:
    spec:
      chart: example
      sourceRef:
        kind: HelmRepository
        namespace: flux-system
        name: example
"""
