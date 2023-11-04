use proconio::input;
use proconio::marker::Chars;
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
        n: Chars
    }
    for i in 1..n.len() {
        let ni_1 = n[i - 1] as usize;
        let ni = n[i] as usize;
        if ni_1 <= ni {
            println!("No");
            return;
        }
    }
    println!("Yes")
}
