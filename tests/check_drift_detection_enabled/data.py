HELM_RELEASE_ENABLED = """
apiVersion: helm.toolkit.fluxcd.io/v2beta2
kind: HelmRelease
metadata:
  name: example
spec:
  driftDetection:
    mode: enabled
"""

HELM_RELEASE_WARN = """
apiVersion: helm.toolkit.fluxcd.io/v2beta2
kind: HelmRelease
metadata:
  name: example
spec:
  driftDetection:
    mode: warn
"""

HELM_RELEASE_MISSING = """
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
