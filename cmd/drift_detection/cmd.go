package drift_detection

import (
	"errors"
	"fmt"
	"io"
	"os"
	"strings"
	"sync"

	"github.com/spf13/cobra"
	"golang.org/x/sync/errgroup"
	"gopkg.in/yaml.v3"
)

func New() *cobra.Command {
	cmd := &cobra.Command{
		Use:   "drift-detection",
		Short: "Checks if HelmReleases have drift detection enabled",
		RunE:  run,
	}
	cmd.Flags().Bool("allow-warn", false, "Allow drift detection warn mode")
	return cmd
}

func run(cmd *cobra.Command, args []string) error {
	allowWarn, err := cmd.Flags().GetBool("allow-warn")
	if err != nil {
		return err
	}

	var errs []error
	var mu sync.Mutex
	var group errgroup.Group
	for _, arg := range args {
		arg := arg
		group.Go(func() error {
			f, err := os.Open(arg)
			if err != nil {
				return err
			}
			defer f.Close()

			if err := checkHelmRelease(f, allowWarn); err != nil {
				mu.Lock()
				errs = append(errs, fmt.Errorf("%w: %s", err, arg))
				mu.Unlock()
			}
			return nil
		})
	}
	if err := group.Wait(); err != nil {
		return err
	}
	return errors.Join(errs...)
}

type HelmRelease struct {
	APIVersion string `yaml:"apiVersion"`
	Kind       string `yaml:"kind"`
	Spec       struct {
		DriftDetection struct {
			Mode string `yaml:"mode"`
		} `yaml:"driftDetection"`
	} `yaml:"spec"`
}

const (
	DriftDetectionEnabled = "enabled"
	DriftDetectionWarn    = "warn"
)

var (
	ErrDriftDetectDisabled = errors.New("HelmRelease drift detection disabled")
	ErrDriftDetectWarn     = errors.New("HelmRelease drift detection warn not allowed")
)

func checkHelmRelease(r io.Reader, allowWarn bool) error {
	decoder := yaml.NewDecoder(r)

	for {
		var release HelmRelease
		if err := decoder.Decode(&release); err != nil {
			if errors.Is(err, io.EOF) {
				return nil
			}
			return err
		}

		if !strings.HasPrefix(release.APIVersion, "helm.toolkit.fluxcd.io/") || release.Kind != "HelmRelease" {
			continue
		}

		switch release.Spec.DriftDetection.Mode {
		case DriftDetectionEnabled:
		case DriftDetectionWarn:
			if !allowWarn {
				return ErrDriftDetectWarn
			}
		default:
			return ErrDriftDetectDisabled
		}
	}
}
