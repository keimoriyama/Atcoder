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
    input! {s:String}
    let set = HashSet::from([
        "ACE".to_string(),
        "BDF".to_string(),
        "CEG".to_string(),
        "DFA".to_string(),
        "EGB".to_string(),
        "FAC".to_string(),
        "GBD".to_string(),
    ]);
    if set.contains(&s) {
        println!("Yes")
    } else {
        println!("No")
    }
}
