pub fn puzzle_1() -> i64 {
    let contents = include_str!("input.txt");

    let mut digits: Vec<Vec<String>> = Vec::new();

    for line in contents.lines() {
        let line_digits: Vec<String> = line.split(" ")
            .map(|x| String::from(x))
            .filter(|x| x != "")
            .collect();
        digits.push(line_digits.clone());

        // for digit in line_digits {
        //     println!("{}",digit)
        // }
    }

    let mut index = 0;

    let mut answers: Vec<i64> = Vec::new();

    while index < digits[0].len() {
        if digits[4][index] == "+" {
            let answer: i64 = digits[0][index].parse::<i64>().unwrap()
                + digits[1][index].parse::<i64>().unwrap()
                + digits[2][index].parse::<i64>().unwrap()
                + digits[3][index].parse::<i64>().unwrap();

            answers.push(answer);
        } else {
            let answer: i64 = digits[0][index].parse::<i64>().unwrap()
                * digits[1][index].parse::<i64>().unwrap()
                * digits[2][index].parse::<i64>().unwrap()
                * digits[3][index].parse::<i64>().unwrap();

            answers.push(answer);
        }

        index += 1;
    }

    // for answer in answers {
    //     println!("{}",answer)
    // }


    answers.iter().sum()
}

pub fn puzzle_2() -> i64 {
    let contents = include_str!("input.txt");

    let mut digits: Vec<Vec<char>> = Vec::new();

    for line in contents.lines() {
        digits.push(line.chars().collect());
    }

    let mut index = 0;
    let mut answer: i64 = 0;
    let mut current_sum: i64 = 0;
    let mut is_addition: bool = false;
    let mut is_multiplication: bool = false;

    while index < digits[0].len() {
        if digits[0][index] == '!'
            && digits[1][index] == '!'
            && digits[2][index] == '!'
            && digits[3][index] == '!'
        {
            answer += current_sum;
            current_sum = 0;
            index += 1;
            continue;
        }

        if digits[0][index] == ' '
            && digits[1][index] == ' '
            && digits[2][index] == ' '
            && digits[3][index] == ' '
        {
            answer += current_sum;
            current_sum = 0;
            index += 1;
            continue;
        }

        if digits[4][index] == '+' {
            is_addition = true;
            is_multiplication = false;
        }

        if digits[4][index] == '*' {
            is_addition = false;
            is_multiplication = true;
        }

        if is_addition {
            current_sum += create_number(vec![
                digits[0][index],
                digits[1][index],
                digits[2][index],
                digits[3][index]
            ])
        }

        if is_multiplication {
            if current_sum == 0 {
                current_sum = 1;
            }

            let num = create_number(vec![
                digits[0][index],
                digits[1][index],
                digits[2][index],
                digits[3][index]
            ]);

            current_sum *= num;
        }

        index += 1;
    }

    answer
}

fn create_number(chars: Vec<char>) -> i64 {
    let mut result: i64 = 0;

    for char in chars {
        if char != ' ' {
            let x = char.to_digit(10).unwrap() as i64;
            result = (result * 10) + x;
        }
    }

    result
}