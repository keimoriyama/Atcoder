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
        n :usize,
        p:[usize;n]
    }
    let mut max = 0;
    let mut max_i = 0;
    for i in 0..n {
        if max <= p[i] {
            max = p[i];
            max_i = i;
        }
    }
    if max_i == 0 {
        println!("0");
    } else {
        println!("{}", max - p[0] + 1)
    }
}
