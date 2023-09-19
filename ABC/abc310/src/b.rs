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
        n:i64,
        m:i64
    }
    let mut c = vec![];
    let mut f = vec![];
    let mut p = vec![];
    for _ in 0..n {
        input! {
            pi:i64,
            ci:i64,
            fi:[i64;ci]
        }
        let fi: HashSet<i64> = fi.into_iter().collect();
        c.push(ci);
        p.push(pi);
        f.push(fi);
    }
    for i in 0..n as usize {
        let pi = p[i];
        let fi = &f[i];
        for j in 0..n as usize {
            let pj = p[j];
            let fj = &f[j];
            if (pi >= pj) && (fj.is_superset(fi)) && (pi > pj || (fj.len() > fi.len())) {
                println!("Yes");
                return;
            }
        }
    }
    println!("No")
}
