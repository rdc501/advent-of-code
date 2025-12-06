pub fn puzzle_1() -> i64 {
    let contents: Vec<&str> = include_str!("./input.txt").lines().collect();

    let mut row_index = 0;
    let mut previous_row = "";
    let mut current_row = contents[row_index];
    let mut next_row = contents[row_index + 1];

    let mut answer = 0;

    while row_index < contents.len() {
        for (column_index, symbol) in current_row.chars().enumerate() {
            if symbol == '@' {
                if can_access(column_index, previous_row.chars().collect(), current_row.chars().collect(), next_row.chars().collect()) {
                    answer += 1;
                }
            }
        }

        row_index += 1;
        previous_row = current_row;
        current_row = next_row;

        if row_index + 1 < contents.len() {
            next_row = contents[row_index + 1];
        } else {
            next_row = "";
        }
    }

    println!("Answer: {}", answer);

    answer
}

pub fn puzzle_2() -> i64 {
    let mut contents: Vec<String> = include_str!("./input.txt").lines().map(|l| String::from(l)).collect();

    let mut total_removed = 0;
    let mut keep_removing = true;

    while keep_removing {
        let (next_contents, removed) = remove_paper(contents.clone());

        total_removed += removed;
        contents = next_contents;
        keep_removing = removed != 0;
    }

    println!("Total removed: {}", total_removed);

    total_removed
}

fn remove_paper(contents: Vec<String>) -> (Vec<String>, i64) {
    let mut row_index = 0;
    let mut previous_row= String::new();
    let mut current_row = contents[row_index].clone();
    let mut next_row = contents[row_index + 1].clone();

    // let mut next_contents: Vec<Vec<char>> = contents.clone().into_iter().map(|s| s.chars().into_iter().collect()).collect();
    let mut next_contents = contents.clone();
    let mut answer = 0;

    while row_index < contents.len() {
        for (column_index, symbol) in current_row.chars().enumerate() {
            if symbol == '@' {
                if can_access(column_index, previous_row.chars().collect(), current_row.chars().collect(), next_row.chars().collect()) {
                    answer += 1;

                    let mut updated_row: Vec<char> = next_contents[row_index].chars().collect();
                    updated_row[column_index] = '.';
                    next_contents[row_index] = updated_row.into_iter().collect();
                }
            }
        }

        row_index += 1;
        previous_row = current_row;
        current_row = next_row;

        if row_index + 1 < contents.len() {
            next_row = contents[row_index + 1].clone();
        } else {
            next_row = String::new();
        }
    }

    println!("Removed: {}", answer);

    (next_contents, answer)
}

fn can_access(index: usize, previous_row: Vec<char>, current_row: Vec<char>, next_row: Vec<char>) -> bool {
    let mut paper_count = 0;

    if previous_row.len() > 0 {
        if index > 0 && previous_row[index - 1] == '@' {
            paper_count += 1;
        }

        if previous_row[index] == '@' {
            paper_count += 1;
        }

        if index < previous_row.len() - 1 && previous_row[index + 1] == '@' {
            paper_count += 1;
        }
    }

    if index > 0 && current_row[index - 1] == '@' {
        paper_count += 1;
    }

    if index < current_row.len() - 1 && current_row[index + 1] == '@' {
        paper_count += 1;
    }

    if next_row.len() > 0 {
        if index > 0 && next_row[index - 1] == '@' {
            paper_count += 1;
        }

        if next_row[index] == '@' {
            paper_count += 1;
        }

        if index < next_row.len() - 1 && next_row[index + 1] == '@' {
            paper_count += 1;
        }
    }

    paper_count < 4
}