use std::collections::{HashMap, HashSet};

pub fn puzzle_1() -> i64 {
    let contents = include_str!("input.txt");

    let mut circuits: Vec<HashSet<&str>> = Vec::new();
    let mut distances : HashMap<String, f64> = HashMap::new();


    for line_a in contents.lines() {
        // Populate the circuits. They all start as size 1
        circuits.push([line_a].into_iter().collect());

        // Populate the distances between each pair of junction boxes
        for line_b in contents.lines() {
            if line_a != line_b {
                distances.insert(
                    calculate_distance_key(line_a, line_b),
                    calculate_distance(line_a, line_b)
                );
            }
        }
    }

    // Sort the distances
    let mut sorted_distances: Vec<_> = distances
        .iter()
        .filter(|(_, v)| !v.is_nan())
        .collect();

    sorted_distances.sort_by(
        |a, b| a.1.partial_cmp(b.1).unwrap()
    );

    // Make the required number of connections between junction boxes
    let mut connections = 0;

    while connections < 1000 {
        let (key, _) = sorted_distances[connections];
        let (a, b) = key.split_once('|').unwrap();

        // Find the existing circuit containing junction box a
        let a_circuit_index = circuits
            .iter()
            .position(|x| x.contains(a))
            .unwrap();

        // Clone the circuit containing junction box a
        let a_circuit = circuits[a_circuit_index].clone();

        // If junction box a is not in the same circuit as b then delete it
        if !a_circuit.contains(b) {
            circuits.remove(a_circuit_index);
        }

        // Find the existing circuit containing junction box b
        let b_circuit_index = circuits
            .iter()
            .position(|x| x.contains(b))
            // .find(|x| x.contains(b))
            .unwrap();

        // Clone the circuit containing junction box b
        let b_circuit = circuits[b_circuit_index].clone();

        // Delete the circuit
        circuits.remove(b_circuit_index);

        // Make a new circuit containing all the values from the existing circuits
        let new_circult: HashSet<&str> = a_circuit
            .into_iter()
            .chain(
                b_circuit
                    .into_iter()
            ).collect();

        circuits.push(new_circult);
        connections += 1;
    }

    for circuit in circuits.clone() {
        println!("{:?}", circuit);
    }

    // Calculate the sizes of the final circuits and sort them in descending order
    let mut circuit_sizes: Vec<i64> = circuits
        .iter()
        .clone()
        .map(|x| x.len() as i64)
        .collect();

circuit_sizes.sort();
circuit_sizes.reverse();

    let answer = circuit_sizes[0] * circuit_sizes[1] * circuit_sizes[2];

    answer
}

fn calculate_distance_key(a: &str, b: &str) -> String {
    if a < b {
        format!("{}|{}", a, b)
    } else {
        format!("{}|{}", b, a)
    }
}

fn calculate_distance(a: &str, b:&str) -> f64 {
    let a_parts: Vec<i64> = a.split(',').map(|x| x.parse().expect("Oops a")).collect();
    let b_parts: Vec<i64> = b.split(',').map(|x| x.parse().expect("Oops b")).collect();

    (
        (
            (a_parts[0] - b_parts[0]).pow(2)
            + (a_parts[1] - b_parts[1]).pow(2)
            + (a_parts[2] - b_parts[2]).pow(2)
        ) as f64
    ).sqrt()
}