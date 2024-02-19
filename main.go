package main

import (
	"fmt"
	"os"

	"github.com/gabe565/pre-commit-fluxcd/cmd"
)

func main() {
	if err := cmd.New().Execute(); err != nil {
		fmt.Println(err.Error())
		os.Exit(1)
	}
}
