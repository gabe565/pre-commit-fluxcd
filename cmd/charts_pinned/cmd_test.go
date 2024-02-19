package charts_pinned

import (
	_ "embed"
	"strings"
	"testing"
)

//go:embed tests/pinned.yaml
var pinned string

//go:embed tests/unpinned.yaml
var unpinned string

//go:embed tests/not_helmrelease.yaml
var notHelmRelease string

var multipleWithUnpinned = pinned + "\n---\n" + unpinned

func Test_checkHelmRelease(t *testing.T) {
	type args struct {
		file string
	}
	tests := []struct {
		name    string
		args    args
		wantErr bool
	}{
		{"pinned", args{pinned}, false},
		{"unpinned", args{unpinned}, true},
		{"multiple_with_unpinned", args{multipleWithUnpinned}, true},
		{"not_helm_release", args{notHelmRelease}, false},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if err := checkHelmRelease(strings.NewReader(tt.args.file)); (err != nil) != tt.wantErr {
				t.Errorf("checkHelmRelease() error = %v, wantErr %v", err, tt.wantErr)
			}
		})
	}
}
