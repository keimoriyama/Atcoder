use proconio::{input, marker::Chars};
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
        m:usize,
        s1: Chars,
        s2: Chars,
        s3: Chars,
    }
    let n: usize = 3;
    let nm = n * m;
    let mut ans: f32 = 1e9;
    for i in 0..nm {
        for j in 0..nm {
            if i == j {
                continue;
            }
            for k in 0..nm {
                if i == k || j == k {
                    continue;
                }
                if (s1[i % m] == s2[j % m]) && (s1[i % m] == s3[k % m]) {
                    ans = ans.min(i.max(j.max(k)) as f32)
                }
            }
        }
    }
    println!("{}", if ans != 1e9 { ans } else { -1 as f32 })
}
