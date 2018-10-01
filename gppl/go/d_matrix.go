// Create a matrix

package main

import (
	"flag"
	"fmt"
)

func main() {
	// Declare command-line arguments
	n := flag.Uint("n", 3, "Number of rows")
	m := flag.Uint("m", 4, "Number of cells")
	d := flag.Int("d", 5, "Cell value")

	// Parse arguments
	flag.Parse()

	// Print matrix
	fmt.Println(Matrix(*n, *m, *d))
}

func Matrix(n uint, m uint, d int) [][]int {
	matrix := make([][]int, n)

	// Create arrays
	for i := uint(0); i < n; i++ {
		// Create sub-arrays
		matrix[i] = make([]int, m)

		for j := uint(0); j < m; j++ {
			// Set values
			matrix[i][j] = d
		}
	}

	return matrix
}
