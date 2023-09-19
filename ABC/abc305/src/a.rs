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
        n: i128
    }
    let mut water = vec![];
    for i in 0..21 {
        water.push(i * 5)
    }
    let mut min_dis = 1000000000000;
    let mut ans = 0;
    for wi in water.iter() {
        if min_dis > (wi - n).abs() {
            // println!("{}", (wi - n).abs());
            min_dis = (wi - n).abs();
            ans = *wi;
        }
    }
    println!("{}", ans);
}
