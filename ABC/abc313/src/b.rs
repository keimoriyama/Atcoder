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
        n:i64,
        m:i64
    }
    let mut s = vec![0; n as usize];
    for _i in 0..m {
        input! {
            _:i64,
            bi:usize
        }
        s[bi - 1] += 1
    }
    // println!("{:?}", s);
    let mut ans: i64 = -1;
    for i in 0..n as usize {
        if s[i] == 0 {
            if ans != -1 {
                println!("-1");
                return;
            } else {
                let i = i as i64;
                ans = i + 1;
            }
        }
    }
    println!("{}", ans)
}
