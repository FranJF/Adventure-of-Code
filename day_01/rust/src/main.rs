fn part_one() -> u32 {
    include_str!("../../input.txt")
        .split("\n\n")
        .map(|e| e.lines().map(|c| c.parse::<u32>().unwrap()).sum::<u32>())
        .max()
        .unwrap()
}
fn part_two() -> u32 {
    let mut cals = include_str!("../../input.txt")
        .split("\n\n")
        .map(|e| e.lines().map(|c| c.parse::<u32>().unwrap()).sum())
        .collect::<Vec<u32>>();
    cals.sort_unstable();
    cals.into_iter().rev().take(3).sum::<u32>()
}

fn main() {
    let part_one = part_one();
    let part_two = part_two();
    println!("Part One: {}", part_one);
    println!("Part Two: {}", part_two);
}
