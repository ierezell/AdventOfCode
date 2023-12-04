use std::{collections::HashMap, fs};

fn part_one() {
    let lines = fs::read_to_string("input.txt").expect("Unable to load input file.");

    let mut sum = 0;
    for line in lines.lines() {
        let numbers: Vec<char> = line.chars().filter(|c| c.is_digit(10)).collect();

        if let (Some(first), Some(last)) = (numbers.first(), numbers.last()) {
            sum += format!("{}{}", first, last)
                .parse::<i32>()
                .expect("Cannot create number from first and last");
        }
    }
    println!("{}", sum)
}

fn part_two() {
    let word_to_digit = HashMap::from([
        ("zero", "ze0o"),
        ("one", "o1e"),
        ("two", "t2o"),
        ("three", "thr3e"),
        ("four", "fo4r"),
        ("five", "fi5e"),
        ("six", "s6x"),
        ("seven", "se7en"),
        ("eight", "ei8ht"),
        ("nine", "n9ne"),
    ]);

    let lines = fs::read_to_string("input.txt").expect("Unable to load input file.");

    let mut sum = 0;
    for line in lines.lines() {
        let mut digit_only_line = line.to_string();
        for (word, digit) in word_to_digit.iter() {
            if digit_only_line.contains(word) {
                digit_only_line = digit_only_line.replace(word, digit);
            }
        }
        let numbers: Vec<char> = digit_only_line.chars().filter(|c| c.is_digit(10)).collect();

        if let (Some(first), Some(last)) = (numbers.first(), numbers.last()) {
            sum += format!("{}{}", first, last)
                .parse::<i32>()
                .expect("Cannot create number from first and last");
        }
    }
    println!("{}", sum)
}

fn main() {
    part_one();
    part_two();
}
