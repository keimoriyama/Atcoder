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
        n:i64,
        s:String,
    }
    for si in s.chars() {
        for _i in 0..2 {
            print!("{}", si)
        }
    }
    println!()
}
