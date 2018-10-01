// Mortgage calculator

package main

import (
	"flag"
	"fmt"
)

func main() {
	// Declare command-line arguments
	value := flag.Float64("value", 2000000, "Value of a mortgage")
	rate := flag.Float64("rate", 10, "Percent rate")
	term := flag.Float64("term", 5, "Mortgage term (years)")

	// Parse arguments
	flag.Parse()

	// Calculate overpayments
	fmt.Printf("%.2f\n", overpayments(*value, *rate / 100.0, *term))
}

func overpayments(value float64, rate float64, term float64) float64 {
	return value * rate * term
}
