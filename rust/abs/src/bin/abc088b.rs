use proconio::input;

fn main() {
    input! {
        n: i32,
        mut a: [i32;n],
    }
    a.sort_by(|a, b| b.cmp(a));
    let alice: i32 = a
        .iter()
        .enumerate()
        .filter(|&(i, &v)| i % 2 == 0)
        .map(|(_, &v)| v)
        .sum();
    let bob: i32 = a
        .iter()
        .enumerate()
        .filter(|&(i, &v)| i % 2 == 1)
        .map(|(_, &v)| v)
        .sum();
    println!("{}", alice - bob);
}
