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
        a:[i128;64]
    }
    let mut base = 1;
    let mut ans: i128 = 0;
    for i in 0..64 {
        ans += base * a[i];
        base *= 2;
    }
    println!("{}", ans)
}
