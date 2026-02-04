use itertools::Itertools;
use proconio::input;

fn main() {
    input! {
        n:usize,
        mut t:[usize;n]
    }
    let mut t_order: Vec<(usize, usize)> = t.iter().enumerate().map(|(i, &v)| (i + 1, v)).collect();
    t_order.sort_by(|a, b| a.1.cmp(&b.1));
    let ans: String = t_order
        .iter()
        .map(|(i, _v)| *i)
        .take(3)
        .join(" ")
        .to_string();
    println!("{}", ans)
}
