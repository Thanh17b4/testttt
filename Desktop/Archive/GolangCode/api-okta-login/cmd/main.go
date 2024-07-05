package main

import (
	"context"
	"github.com/chi07/api-okta-login/internal/http/handler"
	"github.com/chi07/api-okta-login/internal/repository"
	"github.com/chi07/api-okta-login/internal/service"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
	"log"
	"net/http"

	"github.com/chi07/api-okta-login/internal/config"
	"github.com/labstack/echo/v4"
	"github.com/spf13/viper"
)

func main() {
	viper.AutomaticEnv()
	e := echo.New()
	e.GET("/", func(c echo.Context) error {
		return c.String(http.StatusOK, "It works!")
	})
	cnf := config.NewConfig()

	client, err := mongo.Connect(context.Background(), options.Client().ApplyURI(cnf.MongoDB.URI))
	if err != nil {
		log.Fatal("cannot connect to database: " + err.Error())
	}

	db := client.Database(cnf.MongoDB.Database)
	userRepo := repository.NewUserRepository(db)
	oktaService := service.NewOktaService(cnf.Okta, cnf.JWT, userRepo)
	loginHandler := handler.NewLoginHandler(oktaService)

	e.POST("/login", loginHandler.LoginWithOkta)

	log.Println("Server is running on port 8080")
	log.Fatal(http.ListenAndServe(":8080", e))
}
