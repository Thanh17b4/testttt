package utils

import (
	"bufio"
	"fmt"
	"github.com/spf13/viper"
	"log"
	"os"
	"strings"
)

func init() {
	viper.AutomaticEnv()
}

func ParseEnvironment() {
	// useGlobalEnv := true
	if _, err := os.Stat(".env"); os.IsNotExist(err) {
		log.Printf("Environment Variable file (.env) is not present.  Relying on Global Environment Variables")
		// useGlobalEnv = false
	}
	fmt.Println("lll, ", viper.GetString("CLIENT_ID"))
	setEnvVariable("CLIENT_ID", viper.GetString("CLIENT_ID"))
	//setEnvVariable("CLIENT_SECRET", viper.GetString("CLIENT_SECRET"))
	setEnvVariable("ISSUER", viper.GetString("ISSUER"))

	if viper.GetString("CLIENT_ID") == "" {
		log.Printf("Could not resolve a CLIENT_ID environment variable.")
		os.Exit(1)
	}

	//if viper.GetString("CLIENT_SECRET") == "" {
	//	log.Printf("Could not resolve a CLIENT_SECRET environment variable.")
	//	os.Exit(1)
	//}

	if viper.GetString("ISSUER") == "" {
		log.Printf("Could not resolve a ISSUER environment variable.")
		os.Exit(1)
	}
}

func setEnvVariable(env string, current string) {
	if current != "" {
		return
	}

	file, _ := os.Open(".env")
	defer file.Close()

	lookInFile := bufio.NewScanner(file)
	lookInFile.Split(bufio.ScanLines)

	for lookInFile.Scan() {
		parts := strings.Split(lookInFile.Text(), "=")
		key, value := parts[0], parts[1]
		if key == env {
			os.Setenv(key, value)
		}
	}
}
