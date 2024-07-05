package config

import (
	"github.com/spf13/viper"
	"time"
)

type OktaConfig struct {
	ClientID     string
	ClientSecret string
	Issuer       string
	Nonce        string
}

type MongoDBConfig struct {
	URI      string
	Database string
}

type JWTConfig struct {
	SecretKey    string
	ExpiredAfter time.Duration
}

type Config struct {
	MongoDB *MongoDBConfig
	Okta    *OktaConfig
	JWT     *JWTConfig
}

func NewConfig() *Config {
	return &Config{
		MongoDB: &MongoDBConfig{
			URI:      viper.GetString("MONGODB_URI"),
			Database: viper.GetString("MONGODB_DATABASE"),
		},
		Okta: &OktaConfig{
			ClientID:     viper.GetString("OKTA_CLIENT_ID"),
			ClientSecret: viper.GetString("OKTA_CLIENT_SECRET"),
			Issuer:       viper.GetString("OKTA_ISSUER"),
			Nonce:        viper.GetString("OKTA_NONCE"),
		},
		JWT: &JWTConfig{
			SecretKey:    viper.GetString("JWT_SECRET"),
			ExpiredAfter: viper.GetDuration("JWT_EXPIRED_AFTER"),
		},
	}
}
