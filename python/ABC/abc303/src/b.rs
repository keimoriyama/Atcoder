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
        n: usize,
        m:usize,
        a:[[usize;n];m]
    }
    let mut ans = 0;
    for i in 1..(n + 1) {
        for j in (i + 1)..(n + 1) {
            let mut flag = false;
            for k in 0..m {
                for l in 0..(n - 1) {
                    if (a[k][l] == i && a[k][l + 1] == j) || (a[k][l] == j && a[k][l + 1] == i) {
                        flag = true
                    }
                }
            }
            if !flag {
                ans += 1
            }
        }
    }
    println!("{}", ans)
}
