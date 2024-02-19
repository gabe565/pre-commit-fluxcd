package secrets_encrypted

import (
	_ "embed"
	"strings"
	"testing"
)

//go:embed tests/data_invalid.yaml
var dataInvalid string

//go:embed tests/data_valid.yaml
var dataValid string

//go:embed tests/stringdata_invalid.yaml
var stringDataInvalid string

//go:embed tests/stringdata_valid.yaml
var stringDataValid string

func Test_checkYaml(t *testing.T) {
	type args struct {
		file string
	}
	tests := []struct {
		name    string
		args    args
		wantErr bool
	}{
		{"data_valid", args{dataValid}, false},
		{"data_invalid", args{dataInvalid}, true},
		{"stringdata_valid", args{stringDataValid}, false},
		{"stringdata_invalid", args{stringDataInvalid}, true},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if err := checkYaml(strings.NewReader(tt.args.file)); (err != nil) != tt.wantErr {
				t.Errorf("checkYaml() error = %v, wantErr %v", err, tt.wantErr)
			}
		})
	}
}

//go:embed tests/invalid.env
var envInvalid string

//go:embed tests/valid.env
var envValid string

func Test_checkEnv(t *testing.T) {
	type args struct {
		file string
	}
	tests := []struct {
		name    string
		args    args
		wantErr bool
	}{
		{"env_valid", args{envValid}, false},
		{"env_invalid", args{envInvalid}, true},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if err := checkEnv(strings.NewReader(tt.args.file)); (err != nil) != tt.wantErr {
				t.Errorf("checkYaml() error = %v, wantErr %v", err, tt.wantErr)
			}
		})
	}
}
