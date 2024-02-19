package charts_support_renovate

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
		Use:   "charts-support-renovate",
		Short: "Checks if HelmReleases and HelmRepositories are configured to support Renovate",
		RunE:  run,
	}
	return cmd
}

func run(cmd *cobra.Command, args []string) error {
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

			if err := checkHelmRelease(f); err != nil {
				mu.Lock()
				errs = append(errs, fmt.Errorf("%w: %s", err, arg))
				mu.Unlock()
			}

			if _, err := f.Seek(0, io.SeekStart); err != nil {
				return err
			}

			if err := checkHelmRepository(f); err != nil {
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
	Metadata   struct {
		Namespace string `yaml:"namespace"`
	} `yaml:"metadata"`
	Spec struct {
		Chart struct {
			Spec struct {
				SourceRef struct {
					Namespace string `yaml:"namespace"`
				} `yaml:"sourceRef"`
			} `yaml:"spec"`
		} `yaml:"chart"`
	} `yaml:"spec"`
}

func checkHelmRelease(r io.Reader) error {
	decoder := yaml.NewDecoder(r)

	for {
		var release HelmRelease
		if err := decoder.Decode(&release); err != nil {
			if errors.Is(err, io.EOF) {
				break
			}
			return err
		}

		if !strings.HasPrefix(release.APIVersion, "helm.toolkit.fluxcd.io/") || release.Kind != "HelmRelease" {
			continue
		}

		if release.Metadata.Namespace != "" {
			continue
		}
		if release.Spec.Chart.Spec.SourceRef.Namespace != "" {
			continue
		}

		return fmt.Errorf("HelmRelease missing metadata.namespace and spec.chart.spec.sourceRef.namespace")
	}

	return nil
}

type HelmRepository struct {
	APIVersion string `yaml:"apiVersion"`
	Kind       string `yaml:"kind"`
	Metadata   struct {
		Namespace string `yaml:"namespace"`
	} `yaml:"metadata"`
}

func checkHelmRepository(r io.Reader) error {
	decoder := yaml.NewDecoder(r)

	for {
		var release HelmRepository
		if err := decoder.Decode(&release); err != nil {
			if errors.Is(err, io.EOF) {
				break
			}
			return err
		}

		if !strings.HasPrefix(release.APIVersion, "source.toolkit.fluxcd.io/") || release.Kind != "HelmRepository" {
			continue
		}

		if release.Metadata.Namespace != "" {
			continue
		}

		return fmt.Errorf("HelmRepository missing metadata.namespace")
	}

	return nil
}
