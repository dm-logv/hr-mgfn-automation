// People sorter

package main

import (
	"flag"
	"fmt"
)

func main() {
	// Declare command-line arguments
	order := flag.Bool("order", True, "Order: True — by name (asc), False — by age (desc)")

	// Parse arguments
	flag.Parse()
}

type Person struct {
	name string
	age uint
}
