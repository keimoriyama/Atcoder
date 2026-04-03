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
     m:usize,
     s:String,
     c:[usize;n]
    }
    let mut c2idx: Vec<Vec<_>> = vec![vec![]; m + 1];
    for i in 0..n {
        let ci = c[i];
        c2idx[ci].push(i)
    }
    // println!("{:?}", c2idx);
    let mut print_order: Vec<_> = vec!['?'; n];
    let s_vec: Vec<char> = s.chars().collect();
    for i in 1..m + 1 {
        let c2idxi = &c2idx[i];
        for j in 0..c2idxi.len() {
            print_order[c2idxi[(j + 1) % c2idxi.len()]] = s_vec[c2idxi[j]];
        }
    }
    for c in print_order.iter() {
        print!("{}", c)
    }
    println!()
}
