use std::fs;

fn part_one() {
    let data = fs::read_to_string("input.txt").expect("Unable to read file");

    let mut pos = 50;
    let mut pass_by_zero = 0;

    for line in data.lines() {
        let line_chars = line.chars().collect::<Vec<char>>();
        let dir = line_chars[0];
        let value = line_chars[1..]
            .iter()
            .collect::<String>()
            .parse::<i32>()
            .expect("Unable to parse number");

        match dir {
            'L' => pos = (pos - value).rem_euclid(100),
            'R' => pos = (pos + value).rem_euclid(100),
            _ => unreachable!(),
        }

        if pos == 0 {
            pass_by_zero += 1;
        }
    }
    println!("Part one land on zero: {}", pass_by_zero);
}

fn part_two() {
    let data = fs::read_to_string("input.txt").expect("Unable to read file");

    let mut pos = 50;
    let mut pass_by_zero = 0;

    for line in data.lines() {
        let line_chars = line.chars().collect::<Vec<char>>();
        let dir = line_chars[0];
        let value = line_chars[1..]
            .iter()
            .collect::<String>()
            .parse::<i32>()
            .expect("Unable to parse number");

        match dir {
            'L' => {
                let new_pos = pos - value;
                pass_by_zero += value / 100;

                let remainder = value.rem_euclid(100);
                let check_pos = pos - remainder;

                if check_pos <= 0 && pos > 0 {
                    pass_by_zero += 1;
                }
                pos = new_pos.rem_euclid(100);
            }
            'R' => {
                let new_pos = pos + value;
                pass_by_zero += new_pos / 100;
                pos = new_pos.rem_euclid(100);
            }
            _ => unreachable!(),
        }
    }

    println!("Part two Pass by zero: {}", pass_by_zero);
}

fn main() {
    part_one();
    part_two();
}
