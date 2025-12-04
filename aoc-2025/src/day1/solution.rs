pub fn puzzle_1() -> i32 {
    let contents = include_str!("./input.txt");

    let mut current_position = 50;
    let mut password = 0;

    for (index, line) in contents.lines().enumerate() {
        (current_position, password) = puzzle_1_process_line(current_position, password, index, line);
    }

    println!("Final password: {}", password);

    password
}

fn puzzle_1_process_line(current_position: i32, password: i32, index: usize, line: &str) -> (i32, i32) {
    let mut new_current_position = current_position;
    let mut new_password = password;

    let (direction, number_string) = line.split_at(1);

    let number: i32 = number_string.parse().expect("not a number");

    println!("Index: {}, Direction: {}, Number: {}", index, direction, number);

    if direction == "R" {
        new_current_position += number;
    } else {
        new_current_position -= number;
    }

    println!("New position: {}", current_position);

    if new_current_position % 100 == 0 {
        new_password += 1;

        println!("New password: {}", password);
    }

    (new_current_position, new_password)
}

#[cfg(test)]
mod puzzle_1_tests {
    use super::*;

    #[test]
    fn result_is_1092() {
        assert_eq!(puzzle_1(), 1092);
    }
}

pub fn puzzle_2() -> i32 {
    let contents = include_str!("./input.txt");

    let mut current_position = 50;
    let mut password = 0;

    for (index, line) in contents.lines().enumerate() {
        (current_position, password) = puzzle_2_process_line(current_position, password, index, line);
    }

    println!("Final password: {}", password);

    password
}

fn puzzle_2_process_line(current_position: i32, password: i32, index: usize, line: &str) -> (i32, i32) {
    let mut new_current_position = current_position;
    let mut new_password = password;

    let (direction, number_string) = line.split_at(1);

    let mut number: i32 = number_string.parse().expect("not a number");

    println!("Index: {}, Direction: {}, Number: {}", index, direction, number);

    if direction == "R" {
        while number > 0 {
            new_current_position += 1;
            number -= 1;

            if new_current_position == 100 {
                new_current_position = 0;
                new_password += 1;
            }
        }
    } else {
        while number > 0 {
            new_current_position -= 1;
            number -= 1;

            if new_current_position == -1 {
                new_current_position = 99;
            }

            if new_current_position == 0 {
                new_password += 1;
            }
        }
    }

    println!("New position: {}", new_current_position);
    println!("New password: {}", new_password);

    (new_current_position, new_password)
}

#[cfg(test)]
mod puzzle_2_tests {
    use rstest::rstest;
    use super::*;

    #[rstest]
    #[case(1, "R1", 2)]
    #[case(0, "R1", 1)]
    #[case(-1, "R1", 0)]
    #[case(-2, "R1", -1)]
    #[case(2, "L1", 1)]
    #[case(1, "L1", 0)]
    #[case(0, "L1", -1)]
    #[case(-1, "L1", -2)]
    fn changes_position_correctly(
        #[case]current_position: i32,
        #[case]line: &str,
        #[case]expected_position: i32,
    ) {
        let (actual_position, _) = puzzle_2_process_line(current_position, 0, 0, line);
        assert_eq!(actual_position, expected_position);
    }

    #[rstest(::trace)]
    #[case(50, "L68", 1)]
    #[case(82, "L30", 0)]
    #[case(52, "R48", 1)]
    #[case(0, "L5", 0)]
    #[case(95, "R60", 1)]
    #[case(55, "L55", 1)]
    #[case(0, "L1", 0)]
    #[case(99, "L99", 1)]
    #[case(0, "R14", 0)]
    #[case(14, "L82", 1)]
    #[case(0, "R1", 0)]
    #[case(0, "R99", 0)]
    #[case(0, "R100", 1)]
    #[case(99, "R1", 1)]
    #[case(0, "R200", 2)]
    #[case(99, "R101", 2)]
    #[case(99, "R102", 2)]
    #[case(50, "R1000", 10)]
    #[case(0, "L1", 0)]
    #[case(0, "L99", 0)]
    #[case(0, "L100", 1)]
    #[case(0, "L200", 2)]
    #[case(50, "L1000", 10)]
    fn changes_password_correctly(
        #[case]current_position: i32,
        #[case]line: &str,
        #[case]expected_password: i32,
    ) {
        let (_, actual_password) = puzzle_2_process_line(current_position, 0, 0, line);
        assert_eq!(actual_password, expected_password);
    }
}