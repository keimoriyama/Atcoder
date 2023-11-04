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
        x:usize,
        mut a : [i64;n-1]
    }
    a.push(-1);
    let xi = x as i64;
    for last in 0..101 {
        let mut b = a.clone();
        b[n - 1] = last;
        let mut sum = 0;
        let mut ma = 0;
        let mut mi = 100;
        for p in b.iter() {
            sum += p;
            ma = ma.max(*p);
            mi = mi.min(*p);
        }
        let score = sum - ma - mi;
        if score >= xi {
            println!("{}", last);
            return;
        }
    }
    println!("{}", -1)
}
