package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
	"unicode"
)

func part_one() {
	file, err := os.Open("input.txt")
	if err != nil {
		panic(err)
	}

	defer file.Close()

	fileScanner := bufio.NewScanner(file)
	total := 0

	for fileScanner.Scan() {
		line := fileScanner.Text()
		numbers := make([]string, 0)

		for _, char := range line {
			if unicode.IsNumber(char) {
				numbers = append(numbers, string(char))
			}
		}

		if len(numbers) >= 1 {
			var sb strings.Builder
			sb.WriteString(numbers[0])
			sb.WriteString(numbers[len(numbers)-1])

			total_number, err := strconv.Atoi(sb.String())

			if err != nil {
				panic(err)
			} else {
				total += total_number
			}
		}
	}
	fmt.Println(total)
}

func part_two() {
	word_to_digit := map[string]string{
		"zero":  "ze0o",
		"one":   "o1e",
		"two":   "t2o",
		"three": "thr3e",
		"four":  "fo4r",
		"five":  "fi5e",
		"six":   "s6x",
		"seven": "se7en",
		"eight": "ei8ht",
		"nine":  "n9ne",
	}

	file, err := os.Open("input.txt")
	if err != nil {
		panic(err)
	}

	defer file.Close()

	fileScanner := bufio.NewScanner(file)
	total := 0

	for fileScanner.Scan() {
		line := fileScanner.Text()
		numbers := make([]string, 0)

		for key, value := range word_to_digit {
			line = strings.ReplaceAll(line, key, value)
		}

		for _, char := range line {
			if unicode.IsNumber(char) {
				numbers = append(numbers, string(char))
			}
		}

		if len(numbers) >= 1 {
			var sb strings.Builder
			sb.WriteString(numbers[0])
			sb.WriteString(numbers[len(numbers)-1])

			total_number, err := strconv.Atoi(sb.String())

			if err != nil {
				panic(err)
			} else {
				total += total_number
			}
		}
	}
	fmt.Println(total)
}

func main() {
	part_one()
	part_two()
}
