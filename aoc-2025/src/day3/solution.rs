pub fn puzzle_1() -> i64 {
    let contents = include_str!("./input.txt");

    let mut total_joltage = 0;

    for line in contents.lines() {
        total_joltage += get_max_joltage(line.parse().unwrap(), 2);
    }

    println!("Answer: {}", total_joltage);

    total_joltage
}

pub fn puzzle_2() -> i64 {
    let contents = include_str!("./input.txt");

    let mut total_joltage = 0;

    for line in contents.lines() {
        total_joltage += get_max_joltage(line.parse().unwrap(), 12);
    }

    println!("Answer: {}", total_joltage);

    total_joltage
}

fn get_max_joltage(battery_bank: String, number_of_batteries: usize) -> i64 {
    let batteries: Vec<i64> = battery_bank.chars()
        .rev()
        .map(|c| c.to_string().parse().expect("oops"))
        .collect();

    let mut max_index = batteries.len();

    // let number_of_batteries = 2;
    let mut joltages: Vec<i64> = Vec::new();

    while joltages.len() < number_of_batteries {
        let mut joltage = 0;
        let min_index = number_of_batteries - joltages.len() - 1;

        (joltage, max_index) = highest_number(batteries.clone(), min_index, max_index);
        joltages.push(joltage);
    }

    let mut max_joltage = 0;

    for joltage in joltages {
        max_joltage = (max_joltage * 10) + joltage;
    }

    max_joltage
}

fn highest_number(numbers: Vec<i64>, min_index: usize, max_index: usize) -> (i64, usize) {
    let mut result: i64 = 0;
    let mut result_index = 0;

    for (index, number) in numbers.iter().enumerate() {
        if index >= min_index && index < max_index {
            if *number >= result {
                result = *number;
                result_index = index;
            }
        }
    }

    (result, result_index)
}

#[cfg(test)]
mod get_max_joltage_tests {
    use rstest::rstest;
    use super::*;

    #[rstest(::trace)]
    #[case("987654321111111", 2, 98)]
    #[case("811111111111119", 2, 89)]
    #[case("234234234234278", 2, 78)]
    #[case("818181911112111", 2, 92)]
    #[case("00", 2, 0)]
    #[case("12", 2, 12)]
    #[case("21", 2, 21)]
    #[case("123", 2, 23)]
    #[case("213", 2, 23)]
    #[case("312", 2, 32)]
    #[case("132", 2, 32)]
    #[case("231", 2, 31)]
    #[case("321", 2, 32)]
    #[case("3402", 2, 42)]
    #[case("4342", 2, 44)]
    #[case("987654321111111", 12, 987654321111)]
    #[case("811111111111119", 12, 811111111119)]
    #[case("234234234234278", 12, 434234234278)]
    #[case("818181911112111", 12, 888911112111)]
    fn result_is_correct(#[case]battery_bank: String, #[case]number_of_batteries: usize, #[case]expected: i64) {
        assert_eq!(get_max_joltage(battery_bank, number_of_batteries), expected);
    }
}