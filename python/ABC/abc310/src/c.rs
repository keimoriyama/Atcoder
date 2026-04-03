use proconio::input;
// 2分木
// use std::collections::BTreeMap;
// 連想配列
// use std::collections::HashMap;
// 集合
use std::collections::HashSet;
// キュー、スタック
// use std::collections::VecDeque;

fn main() {
    input! {
        n:usize,
        s:[String;n]
    }
    let mut set = HashSet::new();
    for si in s.iter() {
        let rev_si = si.chars().rev().collect::<String>();
        if set.contains(&si) || set.contains(&rev_si) {
            continue;
        }
        set.insert(si);
    }
    println!("{}", set.len())
}
