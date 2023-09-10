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
        n: i32,
    }
    let mut a = vec![];
    for _i in 0..n {
        input! {
            c:usize,
        }
        let mut ai = HashSet::with_capacity(c);
        for _ in 0..c {
            input! {
                a:usize
            }
            ai.insert(a);
        }
        a.push(ai)
    }
    input! {
        x: usize
    }
    let mut min = 40;
    for set in a.iter() {
        if set.contains(&x) {
            min = min.min(set.len())
        }
    }
    if min == 40 {
        println!("0\n");
        return;
    }

    let mut ans = vec![];
    for (i, set) in a.iter().enumerate() {
        if set.contains(&x) && set.len() == min {
            ans.push(i + 1)
        }
    }
    println!("{}", ans.len());
    for i in 0..ans.len() {
        print!("{} ", ans[i])
    }
}
