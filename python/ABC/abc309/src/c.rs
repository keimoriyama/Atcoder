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
        n:usize,
        k:usize
    }
    let mut sumb: usize = 0;
    let mut ab = vec![];
    for _i in 0..n {
        input! {
            ai:usize,
            bi:usize
        }
        sumb += bi;
        ab.push((ai, bi));
    }
    ab.sort();
    if sumb <= k {
        println!("1");
        return;
    }
    for i in 0..n {
        let abi = ab[i];
        // println!("{:?} {}", abi, sumb);
        if k >= sumb {
            println!("{}", ab[i - 1].0 + 1);
            return;
        }
        sumb -= abi.1;
    }
    println!("{}", ab[n - 1].0 + 1);
}
