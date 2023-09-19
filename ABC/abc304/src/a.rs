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
        n: usize
    }
    let mut p = vec![];
    for _i in 0..n {
        input! {
            si:String,
            ai: usize
        }
        p.push((si, ai))
    }
    let mut min_idx: usize = 0;
    let mut min_value: usize = 100000000000;
    for i in 0..n {
        let (_si, ai) = &p[i];
        if &min_value > ai {
            min_value = *ai;
            min_idx = i;
        }
    }
    for i in 0..n {
        if min_idx == 0 {
            println!("{}", p[i].0)
        } else {
            println!("{}", p[(i + min_idx) % n].0)
        }
    }
}
