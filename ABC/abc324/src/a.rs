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
       a: [usize;n]
    }
    let a0 = a[0];
    for i in 1..a.len() {
        if a0 != a[i] {
            println!("No");
            return;
        }
    }
    println!("Yes")
}
