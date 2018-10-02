// Change word declension

package main

import (
	"errors"
	"flag"
	"fmt"
	"strings"
)

func main() {
	// Declare command-line arguments
	word := flag.String("word", "товар", "Word to change declension")
	num := flag.Uint("num", 0, "Number")

	// Parse arguments
	flag.Parse()

	// Get modified word if allowed
	morph, err := MorphWord(*word, *num)
	if err != nil {
		panic(err)
	}
	
	fmt.Println(morph)
}

func MorphWord(word string, num uint) (string, error) {
	if strings.ToLower(word) != "товар" {
		return "", errors.New(fmt.Sprintf("Support of '%s' word is not implemented", word))
	}

	// Last digit of a number
	lastDigit := num % 10
	// Word ending
	end := ""

	if
	// One-word numerics
	(5 <= num && num <= 20) ||
		// Multi-word numerics
		(lastDigit == 0 || 5 <= lastDigit && lastDigit <= 9) {
		end = "ов"
	} else if lastDigit == 1 {
		end = ""
	} else if 2 <= lastDigit && lastDigit <= 4 {
		end = "а"
	}

	return fmt.Sprintf("%d %s%s", num, word, end), nil
}
