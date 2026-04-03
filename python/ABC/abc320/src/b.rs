use proconio::{input, marker::Chars};
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
        s: Chars
    }
    let mut max_len = 0;
    let n = s.len();
    for i in 0..n {
        for j in i + 1..=n {
            let v = s[i..j].iter().collect::<String>();
            let rev = v.chars().rev().collect::<String>();
            if v == rev {
                max_len = max_len.max(j - i);
            }
        }
    }
    println!("{}", max_len)
}
