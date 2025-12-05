pub fn puzzle_1() -> i64 {
    let contents = include_str!("./input.txt");

    let mut total_joltage = 0;

    for line in contents.lines() {
        total_joltage += get_max_joltage(line.parse().unwrap());
    }

    println!("Answer: {}", total_joltage);

    total_joltage
}

fn get_max_joltage(battery_bank: String) -> i64 {
    let mut batteries = battery_bank.chars()
        .rev()
        .map(|c| c.to_string().parse().expect("oops"));

    let mut first = 0;
    let mut second = 0;
    let mut first_index = 0;

    let mut first_batteries = batteries.clone();

    first_batteries.next();

    for (index, battery) in first_batteries.enumerate() {
        if battery >= first {
            // Don't think enumberate() takes into account the next() we did before the loop
            first_index = index + 1;
            first = battery;
        }
    }

    for (index, battery) in batteries.enumerate() {
        if index < first_index {
            if battery > second {
                second = battery
            }
        }
    }

    (first * 10) + second
}

#[cfg(test)]
mod get_max_joltage_tests {
    use rstest::rstest;
    use super::*;

    #[rstest(::trace)]
    #[case("987654321111111", 98)]
    #[case("811111111111119", 89)]
    #[case("234234234234278", 78)]
    #[case("818181911112111", 92)]
    #[case("00", 0)]
    #[case("12", 12)]
    #[case("21", 21)]
    #[case("123", 23)]
    #[case("213", 23)]
    #[case("312", 32)]
    #[case("132", 32)]
    #[case("231", 31)]
    #[case("321", 32)]

    #[case("3402", 42)]
    #[case("4342", 44)]
    fn result_is_correct(#[case]battery_bank: String, #[case]expected: i64) {
        assert_eq!(get_max_joltage(battery_bank), expected);
    }
}