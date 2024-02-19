package secrets_encrypted

import (
	"bufio"
	"bytes"
	"errors"
	"fmt"
	"io"
	"os"
	"path/filepath"
	"strings"
	"sync"

	"github.com/spf13/cobra"
	"golang.org/x/sync/errgroup"
	"gopkg.in/yaml.v3"
)

func New() *cobra.Command {
	cmd := &cobra.Command{
		Use:   "secrets-encrypted",
		Short: "Checks if secrets and envs are encrypted",
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

			switch filepath.Ext(arg) {
			case ".yml", ".yaml":
				if err := checkYaml(f); err != nil {
					mu.Lock()
					errs = append(errs, fmt.Errorf("%w: %s", err, arg))
					mu.Unlock()
				}
			case ".env":
				if err := checkEnv(f); err != nil {
					mu.Lock()
					errs = append(errs, fmt.Errorf("%w: %s", err, arg))
					mu.Unlock()
				}
			}
			return nil
		})
	}
	if err := group.Wait(); err != nil {
		return err
	}
	return errors.Join(errs...)
}

type Secret struct {
	APIVersion string             `yaml:"apiVersion"`
	Kind       string             `yaml:"kind"`
	Data       *map[string]string `yaml:"data"`
	StringData *map[string]string `yaml:"stringData"`
	Sops       *map[string]any    `yaml:"sops"`
}

var ErrSecretDecrypted = errors.New("secret file decrypted")

func checkYaml(r io.Reader) error {
	decoder := yaml.NewDecoder(r)

	for {
		var secret Secret
		if err := decoder.Decode(&secret); err != nil {
			if errors.Is(err, io.EOF) {
				return nil
			}
			return err
		}

		if !strings.HasPrefix(secret.APIVersion, "v1") || secret.Kind != "Secret" {
			continue
		}

		if secret.Data == nil && secret.StringData == nil {
			continue
		}

		if secret.Sops == nil {
			return ErrSecretDecrypted
		}
	}
}

var ErrEnvDecrypted = errors.New("env file decrypted")

func checkEnv(r io.Reader) error {
	scanner := bufio.NewScanner(r)
	for scanner.Scan() {
		if bytes.HasPrefix(scanner.Bytes(), []byte("sops_mac=")) {
			return nil
		}
	}
	if scanner.Err() != nil {
		return scanner.Err()
	}
	return ErrEnvDecrypted
}
