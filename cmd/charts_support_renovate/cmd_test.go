package charts_support_renovate

import (
	_ "embed"
	"strings"
	"testing"
)

//go:embed tests/helmrelease_metadata_valid.yaml
var helmReleaseMetadataValid string

//go:embed tests/helmrelease_sourceref_valid.yaml
var helmReleaseSourceRefValid string

//go:embed tests/helmrelease_invalid.yaml
var helmReleaseInvalid string

//go:embed tests/not_helmrelease.yaml
var configMap string

func Test_checkHelmRelease(t *testing.T) {
	type args struct {
		file string
	}
	tests := []struct {
		name    string
		args    args
		wantErr bool
	}{
		{"helmrelease_metadata_valid", args{helmReleaseMetadataValid}, false},
		{"helmrelease_sourceref_valid", args{helmReleaseSourceRefValid}, false},
		{"helmrelease_invalid", args{helmReleaseInvalid}, true},
		{"not_helmrelease", args{configMap}, false},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if err := checkHelmRelease(strings.NewReader(tt.args.file)); (err != nil) != tt.wantErr {
				t.Errorf("checkHelmRelease() error = %v, wantErr %v", err, tt.wantErr)
			}
		})
	}
}

//go:embed tests/helmrepository_valid.yaml
var helmRepositoryValid string

//go:embed tests/helmrepository_invalid.yaml
var helmRepositoryInvalid string

func Test_checkHelmRepository(t *testing.T) {
	type args struct {
		file string
	}
	tests := []struct {
		name    string
		args    args
		wantErr bool
	}{
		{"helmrepository_valid", args{helmRepositoryValid}, false},
		{"helmrepository_invalid", args{helmRepositoryInvalid}, true},
		{"not_helmrepository", args{configMap}, false},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if err := checkHelmRepository(strings.NewReader(tt.args.file)); (err != nil) != tt.wantErr {
				t.Errorf("checkHelmRepository() error = %v, wantErr %v", err, tt.wantErr)
			}
		})
	}
}
