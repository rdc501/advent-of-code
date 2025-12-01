pub fn puzzle_1 () {
    let contents = include_str!("./input.txt");

    let mut current_position = 50;
    let mut password = 0;

    for (index, line) in contents.lines().enumerate() {
        let (direction, number_string) = line.split_at(1);

        let number: i32 = number_string.parse().expect("not a number");

        println!("Index: {}, Direction: {}, Number: {}", index, direction, number);

        if direction == "R" {
            current_position += number;
        } else {
            current_position -= number;
        }

        println!("New position: {}", current_position);

        if (current_position % 100 == 0) {
            password += 1;

            println!("New password: {}", password);
        }
    }

    println!("Final password: {}", password);
}