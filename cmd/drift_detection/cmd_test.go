package drift_detection

import (
	_ "embed"
	"strings"
	"testing"
)

//go:embed tests/enabled.yaml
var enabled string

//go:embed tests/warn.yaml
var warn string

//go:embed tests/missing.yaml
var missing string

func Test_checkHelmRelease(t *testing.T) {
	type args struct {
		file      string
		allowWarn bool
	}
	tests := []struct {
		name    string
		args    args
		wantErr bool
	}{
		{"enabled", args{file: enabled}, false},
		{"warn_allowed", args{file: warn, allowWarn: true}, false},
		{"warn_not_allowed", args{file: warn}, true},
		{"missing", args{file: missing}, true},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if err := checkHelmRelease(strings.NewReader(tt.args.file), tt.args.allowWarn); (err != nil) != tt.wantErr {
				t.Errorf("checkHelmRelease() error = %v, wantErr %v", err, tt.wantErr)
			}
		})
	}
}
