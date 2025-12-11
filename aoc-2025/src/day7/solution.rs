use std::collections::HashSet;

pub fn puzzle_1 () -> i64 {
    let contents = include_str!("input.txt");

    let mut answer = 0;
    let mut beam_columns: HashSet<i64> = HashSet::new();

    for line in contents.lines() {
        for (index, c) in line.chars().enumerate() {
            let i = index as i64;

            if c == 'S' {
                beam_columns.insert(i);
            }

            if c == '^' {
                if beam_columns.contains(&i) {
                    beam_columns.remove(&i);
                    beam_columns.insert(i - 1);
                    beam_columns.insert(i + 1);

                    answer += 1;
                }
            }
        }
    }

    answer
}