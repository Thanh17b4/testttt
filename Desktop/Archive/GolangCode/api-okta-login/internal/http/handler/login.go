package handler

import (
	"github.com/chi07/api-okta-login/internal/http/request"
	"github.com/labstack/echo/v4"
	"log"
	"net/http"
)

type LoginHandler struct {
	oktaService OktaService
}

func NewLoginHandler(authService OktaService) *LoginHandler {
	return &LoginHandler{oktaService: authService}
}

func (h *LoginHandler) LoginWithOkta(c echo.Context) error {
	var req request.LoginRequest

	if err := c.Bind(&req); err != nil {
		log.Fatal("failed to bind request: " + err.Error())
		return c.JSON(http.StatusBadRequest, map[string]interface{}{
			"message": err.Error(),
			"code":    http.StatusBadRequest,
		})
	}
	token, err := h.oktaService.Login(req.OktaToken)
	if err != nil {

		return c.JSON(http.StatusUnauthorized, "error: token invalid or expired"+err.Error())
	}

	return c.JSON(http.StatusOK, token)

}
