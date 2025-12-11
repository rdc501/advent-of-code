use std::collections::{HashMap, HashSet};

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

pub fn puzzle_2_slow () -> i64 {
    let contents = include_str!("input.txt");

    let mut paths: Vec<Vec<i64>> = Vec::new();

    for line in contents.lines() {
        for (index, c) in line.chars().enumerate() {
            let i = index as i64;

            if c == 'S' {
                paths.push(vec![i])
            }

            if c == '^' {
                for (path_index, path) in paths.clone().iter().enumerate() {
                    if path.last() == Some(&i) {
                        println!("Index: {}, Matching path: {:?}", i, path);

                        paths.remove(path_index);
                        paths.push([&path[..], &[i - 1]].concat());
                        paths.push([&path[..], &[i + 1]].concat());
                    }
                }
            }
        }
    }

    paths.len() as i64
}
pub fn puzzle_2 () -> i64 {
    let contents = include_str!("input.txt");

    let mut path_ends: HashMap<i64, i64> = HashMap::new();

    for line in contents.lines() {
        for (index, c) in line.chars().enumerate() {
            let i = index as i64;

            if c == 'S' {
                path_ends.insert(i, 1);
            }

            if c == '^' {
                if path_ends.contains_key(&i) {
                    let num = *path_ends.get(&i).unwrap();

                    *path_ends.entry(i - 1).or_insert(0) += num;
                    *path_ends.entry(i + 1).or_insert(0) += num;

                    path_ends.remove(&i);
                }
            }
        }
    }

    path_ends.values().sum()
}