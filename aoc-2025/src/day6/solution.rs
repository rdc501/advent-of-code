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