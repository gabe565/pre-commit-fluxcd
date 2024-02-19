package cmd

import (
	"github.com/gabe565/pre-commit-fluxcd/cmd/charts_pinned"
	"github.com/gabe565/pre-commit-fluxcd/cmd/charts_support_renovate"
	"github.com/gabe565/pre-commit-fluxcd/cmd/drift_detection"
	"github.com/gabe565/pre-commit-fluxcd/cmd/secrets_encrypted"
	"github.com/spf13/cobra"
)

func New() *cobra.Command {
	cmd := &cobra.Command{
		Use:   "pre-commit-fluxcd",
		Short: "Pre-Commit hooks for GitOps repositories",

		SilenceUsage:  true,
		SilenceErrors: true,
	}

	cmd.AddCommand(
		charts_pinned.New(),
		charts_support_renovate.New(),
		drift_detection.New(),
		secrets_encrypted.New(),
	)
	return cmd
}
