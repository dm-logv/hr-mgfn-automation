// People sorter

package main

import (
	"flag"
	"fmt"
	"math/rand"
	"sort"
)

func main() {
	// Declare command-line arguments
	order := flag.String("order", "name", "(name | age) Order by name (asc) or by age (desc)")

	// Parse arguments
	flag.Parse()

	// Create People Storage
	population := GeneratePeople()

	// Extract ordering type from argument
	switch *order {
	case "name":
		population.byName()
	case "age":
		
		population.byAge()
	default:
		panic(fmt.Sprintf("Sort by '%s' is not implemented", *order))
	}

	fmt.Println(population)
}

// Human struct
type Person struct {
	Name string
	Age  uint
}

// Humans' storage
type Storage []Person

// Storage sorting function: by name (asc)
func (s Storage) byName() {
	sort.Slice(s, func(i, j int) bool {
		return s[i].Name < s[j].Name
	})
}

// Storage sorting function: by age (desc)
func (s Storage) byAge() {
	sort.Slice(s, func(i, j int) bool {
		return s[i].Age > s[j].Age
	})
}

// Generate population
func GeneratePeople() Storage {
	storage := Storage{
		Person{Name: "Lance Paul", Age: uint(rand.Int31n(100))},
		Person{Name: "Frederick Tucker", Age: uint(rand.Int31n(100))},
		Person{Name: "Patsy Owens", Age: uint(rand.Int31n(100))},
		Person{Name: "Pearl Lawrence", Age: uint(rand.Int31n(100))},
		Person{Name: "Christina Zimmerman", Age: uint(rand.Int31n(100))},
		Person{Name: "Al Sharp", Age: uint(rand.Int31n(100))},
		Person{Name: "Kent Larson", Age: uint(rand.Int31n(100))},
		Person{Name: "Francis Salazar", Age: uint(rand.Int31n(100))},
		Person{Name: "Dora Santiago", Age: uint(rand.Int31n(100))},
		Person{Name: "Jenna Caldwell", Age: uint(rand.Int31n(100))},
		Person{Name: "Joseph Patton", Age: uint(rand.Int31n(100))},
		Person{Name: "Irene Day", Age: uint(rand.Int31n(100))},
		Person{Name: "Katrina Ward", Age: uint(rand.Int31n(100))},
		Person{Name: "Guadalupe Guerrero", Age: uint(rand.Int31n(100))},
		Person{Name: "Melba Nash", Age: uint(rand.Int31n(100))},
		Person{Name: "Carol Christensen", Age: uint(rand.Int31n(100))},
		Person{Name: "Amelia Wilkins", Age: uint(rand.Int31n(100))},
		Person{Name: "Leigh Jensen", Age: uint(rand.Int31n(100))},
		Person{Name: "Jay Dawson", Age: uint(rand.Int31n(100))},
		Person{Name: "Cora Pearson", Age: uint(rand.Int31n(100))},
		Person{Name: "Lorraine Schwartz", Age: uint(rand.Int31n(100))},
		Person{Name: "Jeffery Gonzalez", Age: uint(rand.Int31n(100))},
		Person{Name: "Marty Hamilton", Age: uint(rand.Int31n(100))},
		Person{Name: "Stewart Ferguson", Age: uint(rand.Int31n(100))},
		Person{Name: "Erin Burns", Age: uint(rand.Int31n(100))}}

	return storage
}
