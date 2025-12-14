use itertools::Itertools;


pub fn puzzle_1() -> i64 {
    let contents = include_str!("input.txt");

    let mut square_locations: Vec::<(i64, i64)> = Vec::new();
    let mut rectange_sizes: Vec::<i64> = Vec::new();

    for line in contents.lines() {
        let (x, y) = line.split_once(',').unwrap();

        square_locations.push((x.parse::<i64>().unwrap(), y.parse::<i64>().unwrap()));
    }

    for combination in square_locations.iter().combinations(2) {
        let (x1, y1) = *combination[0];
        let (x2, y2) = *combination[1];

        rectange_sizes.push(calculate_rectangle(x1, x2, y1, y2));
    }

    rectange_sizes.sort();

    *rectange_sizes.last().unwrap()
}

fn calculate_rectangle(x1: i64, x2:i64, y1:i64, y2: i64) -> i64 {
    ((x1 - x2).abs() + 1) * ((y1 - y2).abs() + 1)
}