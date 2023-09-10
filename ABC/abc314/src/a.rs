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
    input! {n:usize}
    let pi = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679";
    println!("{}", &pi[..n + 2]);
}
