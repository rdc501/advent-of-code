pub fn puzzle_1() -> i64 {
    let contents: Vec<&str> = include_str!("./input.txt").lines().collect();

    let (fresh_ranges, ingredients) = process_input(contents);

    let mut number_of_fresh = 0;

    for ingredient in ingredients {
        for range in fresh_ranges.clone() {
            if ingredient >= range.0 && ingredient <= range.1 {
                number_of_fresh += 1;
                break
            }
        }
    }

    println!("Answer: {}", number_of_fresh);

    number_of_fresh
}

fn process_input(input: Vec<&str>) -> (Vec<(i64, i64)>, Vec<i64>) {
    let mut fresh_ranges = Vec::new();
    let mut ingredients = Vec::new();

    for line in input {
        if line.contains('-') {
            let ids = line.split_once('-').unwrap();

            fresh_ranges.push((
                ids.0.parse().unwrap(),
                ids.1.parse().unwrap()
            ));
        } else {
            if line.ne("") {
                ingredients.push(line.parse().unwrap());
            }
        }
    }

    (fresh_ranges, ingredients)
}