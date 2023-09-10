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
        m: i64,
        d: [i64;m]
    }
    let mut total = 0;
    for i in 0..m as usize {
        total += d[i];
    }
    let mut mid = (total + 1) / 2;
    for i in 0..m as usize {
        if mid <= d[i] {
            println!("{} {}", i + 1, mid);
            return;
        } else {
            mid -= d[i]
        }
    }
}
