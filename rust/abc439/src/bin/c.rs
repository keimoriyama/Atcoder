use itertools::Itertools;
use num_integer::Roots;
use proconio::input;

fn main() {
    input! {
        n:usize
    }
    let mut c = vec![0; n + 1];
    let sqrt_n = n.sqrt() + 1;
    //println!("{}", sqrt_n);
    for x in 1..sqrt_n {
        for y in (x + 1)..sqrt_n {
            let idx = x.pow(2) + y.pow(2);
            if idx > n {
                continue;
            }
            c[idx] += 1;
        }
    }
    let mut tmp_ans: Vec<usize> = c
        .iter()
        .enumerate()
        .filter(|&(i, &v)| v == 1)
        .map(|(i, _)| i)
        .collect();
    let ans = tmp_ans.iter().join(" ");
    let ans_n = tmp_ans.len();
    println!("{}", ans_n);
    println!("{}", ans);
}
