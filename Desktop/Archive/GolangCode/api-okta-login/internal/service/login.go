package service

import (
	"github.com/chi07/api-okta-login/internal/config"
	"github.com/chi07/api-okta-login/internal/repository"
	"github.com/dgrijalva/jwt-go"
	jwtverifier "github.com/okta/okta-jwt-verifier-golang/v2"
	"log"
	"time"
)

type OktaService struct {
	oktaConfig *config.OktaConfig
	jwtConfig  *config.JWTConfig
	userRepo   *repository.UserRepository
}

func NewOktaService(oktaConfig *config.OktaConfig, jwtConfig *config.JWTConfig, userRepo *repository.UserRepository) *OktaService {
	return &OktaService{
		oktaConfig: oktaConfig,
		jwtConfig:  jwtConfig,
		userRepo:   userRepo,
	}
}

func (s *OktaService) Login(oktaToken string) (string, error) {
	claims, ok, err := s.VerifyToken(oktaToken)
	if err != nil {
		log.Fatal("failed to verify token: " + err.Error())
		return "", err
	}
	if !ok {
		log.Fatal("failed to verify token: " + err.Error())
	}

	username := claims.Claims["sub"].(string)
	if username == "" {
		log.Fatal("failed to get username from token" + err.Error())
		return "", err
	}

	email := claims.Claims["email"].(string)
	if email == "" {
		log.Fatal("failed to get email from token" + err.Error())
		return "", err
	}

	name := claims.Claims["name"].(string)
	if name == "" {
		log.Fatal("failed to get name from token" + err.Error())
		return "", err
	}

	oktaID := name

	accessToken, err := s.GenerateToken(username, email, oktaID)
	if err != nil {
		return "", err
	}

	return accessToken, nil
}

var jwtKey = []byte("your_secret_key")

type Claims struct {
	Username string `json:"username"`
	OkID     string `json:"okta_id"`
	Email    string `json:"email"`
	jwt.StandardClaims
}

func (s *OktaService) VerifyToken(reqToken string) (*jwtverifier.Jwt, bool, error) {
	toValidate := map[string]string{}
	toValidate["aud"] = s.oktaConfig.ClientID
	toValidate["nonce"] = "nonce"

	jwtVerifierSetup := jwtverifier.JwtVerifier{
		Issuer:           s.oktaConfig.Issuer,
		ClaimsToValidate: toValidate,
	}

	verifier, err := jwtVerifierSetup.New()
	if err != nil {
		log.Fatal("failed to create verifier: " + err.Error())
		return nil, false, err
	}

	token, err := verifier.VerifyAccessToken(reqToken)
	if err != nil {
		log.Fatal("failed to verify token: " + err.Error())
		return nil, false, err
	}

	return token, true, nil
}

func (s *OktaService) GenerateToken(username, email, oktaID string) (string, error) {
	expirationTime := time.Now().Add(time.Second * s.jwtConfig.ExpiredAfter).Unix()
	claims := &Claims{
		Username: username,
		OkID:     oktaID,
		Email:    email,
		StandardClaims: jwt.StandardClaims{
			ExpiresAt: expirationTime,
			IssuedAt:  time.Now().Unix(),
		},
	}

	token := jwt.NewWithClaims(jwt.SigningMethodHS256, claims)
	tokenString, err := token.SignedString(jwtKey)
	if err != nil {
		return "", err
	}
	return tokenString, nil
}
