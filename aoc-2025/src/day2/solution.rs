pub fn puzzle_1() -> i64 {
    let contents = include_str!("./input.txt");

    let line = contents.lines().next().unwrap().to_string();
    let ranges_as_strings = line.split(",");

    let mut ranges: Vec<(i64, i64)> = Vec::new();

    for range_string in ranges_as_strings {
        let mut x = range_string.split('-');

        ranges.push(
            (
            x.next().unwrap().to_string().parse().expect("String could not be parsed as a number"),
            x.next().unwrap().to_string().parse().expect("String could not be parsed as a number")
            )
        );
    }

    let mut answer: i64 = 0;

    for range in ranges {
        println!("{} {}", range.0, range.1);

        let mut current = range.0;

        while current <= range.1 {
            if !is_id_valid(current) {
                answer += current;
            }

            current += 1;
        }
    }

    println!("Answer: {}", answer);

    return answer;
}

fn is_id_valid(id: i64) -> bool {
    let id_string = id.to_string();
    let number_of_characters = id_string.chars().count();
    let midpoint = number_of_characters / 2;

    if number_of_characters == 1 || number_of_characters % 2 == 1 {
        return true;
    }

    let (first, second) = id_string.split_at(midpoint);

    if first == second {
        return false;
    }

    return true;
}

#[cfg(test)]
mod is_id_valid_tests {
    use rstest::rstest;
    use super::*;

    #[rstest(::trace)]
    #[case(0, true)]
    #[case(1, true)]
    #[case(9, true)]
    #[case(10, true)]
    #[case(11, false)]
    #[case(99, false)]
    #[case(999, true)]
    #[case(1010, false)]
    #[case(1011, true)]
    #[case(9999, false)]
    fn result_is_correct(#[case]id: i64, #[case]expected: bool) {
        assert_eq!(is_id_valid(id), expected);
    }
}

pub fn puzzle_2() -> i64 {
    let contents = include_str!("./input.txt");

    let line = contents.lines().next().unwrap().to_string();
    let ranges_as_strings = line.split(",");

    let mut ranges: Vec<(i64, i64)> = Vec::new();

    for range_string in ranges_as_strings {
        let mut x = range_string.split('-');

        ranges.push(
            (
                x.next().unwrap().to_string().parse().expect("String could not be parsed as a number"),
                x.next().unwrap().to_string().parse().expect("String could not be parsed as a number")
            )
        );
    }

    let mut answer: i64 = 0;

    for range in ranges {
        println!("{} {}", range.0, range.1);

        let mut current = range.0;

        while current <= range.1 {
            if !is_id_valid_2(current) {
                answer += current;
            }

            current += 1;
        }
    }

    println!("Answer: {}", answer);

    return answer;
}

fn is_id_valid_2(id: i64) -> bool {
    let id_string = id.clone().to_string();
    let number_of_characters = id_string.chars().count();
    let mut group_size  = number_of_characters / 2;

    while group_size > 0 {
        if number_of_characters % group_size == 0 {
            let valid = is_id_valid_with_group_size(id_string.clone(), number_of_characters, group_size);

            if !valid {
                return false;
            }
        }

        group_size -= 1;
    }

    return true;
}

fn is_id_valid_with_group_size(id_string: String, number_of_characters: usize, group_size: usize) -> bool {
    let mut groups = Vec::new();
    let split_point = group_size;
    // println!("Group size: {}, Split point: {}", group_size, split_point);

    let mut previous_split_point = 0;

    while previous_split_point + split_point <= number_of_characters {
        let (group, remaining) = id_string.split_at(previous_split_point).1.split_at(split_point);

        // println!("Group: {}, Remaining: {}", group, remaining);

        groups.push(group);

        previous_split_point += split_point;
    }

    // for (_, group) in groups.iter().enumerate() {
    //     println!("Group: {}", group);
    // }

    return !groups.iter().all(|s| s == &groups[0]);
}

#[cfg(test)]
mod is_id_valid_2_tests {
    use rstest::rstest;
    use super::*;

    #[rstest(::trace)]
    #[case(0, true)]
    #[case(1, true)]
    #[case(9, true)]
    #[case(10, true)]
    #[case(11, false)]
    #[case(99, false)]
    #[case(999, false)]
    #[case(1010, false)]
    #[case(1011, true)]
    #[case(9999, false)]
    #[case(565656, false)]
    #[case(565651, true)]
    fn result_is_correct(#[case]id: i64, #[case]expected: bool) {
        assert_eq!(is_id_valid_2(id), expected);
    }
}