use proconio::input;
// 2分木
// use std::collections::BTreeMap;
// 連想配列
// use std::collections::HashMap;
// 集合
// use std::collections::HashSet;
// キュー、スタック
// use std::collections::VecDeque;

fn main() {
    input! {
        n: usize,
        p: usize,
        q:usize,
        d: [usize;n]
    }
    let min_d = d.iter().min().unwrap();
    if min_d + q < p {
        println!("{}", min_d + q)
    } else {
        println!("{}", p)
    }
}
