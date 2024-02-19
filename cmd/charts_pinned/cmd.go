package charts_pinned

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
		Use:   "charts-pinned",
		Short: "Checks if HelmReleases are pinned",
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
		Chart struct {
			Spec struct {
				Version string `yaml:"version"`
			} `yaml:"spec"`
		} `yaml:"chart"`
	} `yaml:"spec"`
}

var ErrReleaseMissingVersion = errors.New("HelmRelease missing version")

func checkHelmRelease(r io.Reader) error {
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

		if release.Spec.Chart.Spec.Version == "" {
			return ErrReleaseMissingVersion
		}
	}
}
