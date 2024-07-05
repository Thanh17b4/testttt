package handler

import jwtverifier "github.com/okta/okta-jwt-verifier-golang/v2"

type OktaService interface {
	Login(oktaToken string) (string, error)
	VerifyToken(reqToken string) (*jwtverifier.Jwt, bool, error)
}
