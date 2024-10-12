package main

import (
	"fmt"
	"math"
)

func formatFloat(value float64) string {
	// Kiểm tra nếu giá trị là số nguyên
	if value == math.Floor(value) {
		// Nếu là số nguyên, trả về dưới dạng số nguyên
		return fmt.Sprintf("%.0f", value)
	} else {
		// Nếu có phần thập phân, làm tròn đến 2 chữ số sau dấu phẩy
		return fmt.Sprintf("%.2f", value)
	}
}

func main() {
	// Các giá trị cần định dạng
	var value1, value2 float64
	value1 = 123
	value2 = 231.06

	// In ra giá trị đã định dạng
	a := fmt.Sprintf("%s, %s\n", formatFloat(value1), formatFloat(value2))
	fmt.Println("a: ", a)
}
