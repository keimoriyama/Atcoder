use proconio::input;
// 2分木
use std::collections::BTreeMap;
// 連想配列
use std::collections::HashMap;
// 集合
use std::collections::HashSet;
// キュー、スタック
use std::collections::VecDeque;

fn main() {
    input! {
        mut n: i64,
        m: i64,
        p: i64
    }
    let mut ans = 0;
    n += 1;
    for i in (m..n).step_by(p as usize) {
        ans += 1;
    }
    println!("{}", ans)
}
