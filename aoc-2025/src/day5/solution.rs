pub fn puzzle_1() -> i64 {
    let contents: Vec<&str> = include_str!("input.txt").lines().collect();

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

pub fn puzzle_2() -> i64 {
    let contents: Vec<&str> = include_str!("input.txt").lines().collect();

    let (fresh_ranges, _) = process_input(contents);
    let mut current_ranges = fresh_ranges;

    let mut keep_consolidating = true;
    let mut answer = 0;

    while keep_consolidating {
        let consolidated_ranges = consolidate_ranges(current_ranges.clone());

        println!("Number of ranges: {}", consolidated_ranges.len());
        for range in consolidated_ranges.clone() {
            println!("Range: {} - {}", range.0, range.1);
        }

        if consolidated_ranges.len() == current_ranges.len() {
            keep_consolidating = false
        } else {
            current_ranges = consolidated_ranges;
        }
    }

    for range in current_ranges {
        answer += range.1 - range.0 + 1;
    }

    println!("Answer: {}", answer);

    answer
}

fn consolidate_ranges(ranges: Vec<(i64, i64)>) -> Vec<(i64, i64)> {
    let mut consolidated_ranges: Vec<(i64, i64)> = Vec::new();

    for range in ranges {
        let mut index = 0;
        let mut updated = false;

        while index < consolidated_ranges.len() {
            let mut consolidated_range = consolidated_ranges[index];

            // Range extends the consolidated range downwards
            if range.0 < consolidated_range.0
                && range.1 >= consolidated_range.0
                &&  range.1 <= consolidated_range.1
            {
                consolidated_ranges[index].0 = range.0;
                updated = true;
            }

            // Range extends the consolidated range upwards
            if range.0 >= consolidated_range.0
                && range.0 <= consolidated_range.1
                && range.1 > consolidated_range.1
            {
                consolidated_ranges[index].1 = range.1;
                updated = true;
            }

            // Range extends the consolidated range in both directions
            if range.0 < consolidated_range.0
                && range.1 > consolidated_range.1
            {
                consolidated_ranges[index].0 = range.0;
                consolidated_ranges[index].1 = range.1;
                updated = true;
            }

            // Range is totally within the consolidated range
            if range.0 >= consolidated_range.0
                && range.1 <= consolidated_range.1
            {
                // This is a lie but we don't want the range adding
                // to the consolidated ranges
                updated = true
            }

            index += 1;
        }

        if !updated {
            consolidated_ranges.push(range);
        }
    }

    consolidated_ranges
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