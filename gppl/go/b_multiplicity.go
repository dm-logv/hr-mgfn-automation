// Multiplicity

package main

import (
	"flag"
	"fmt"
)

func main() {
	// Declare command-line arguments
	min := flag.Int("min", 45, "Minimal range value")
	max := flag.Int("max", 670, "Maximum range value")
	multiplicity := flag.Int("multiplicity", 10, "Multiplicity")

	// Parse arguments
	flag.Parse()

	// Print multiples
	fmt.Println(Multiples(*min, *max, *multiplicity))
}

func Multiples(min int, max int, multiplicity int) []int {
	var multiples []int

	// Include minimal value to result
	min_multiple := min - 1

	for min_multiple <= max {
		// Find next multiple
		next_multiple := (min_multiple + multiplicity - (min_multiple % multiplicity))

		if next_multiple <= max {
			// Add to result, if not out of range
			multiples = append(multiples, next_multiple)
		}

		min_multiple = next_multiple
	}

	return multiples
}
