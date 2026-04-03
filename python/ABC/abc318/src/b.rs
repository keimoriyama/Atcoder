use proconio::input;
// 2分木
use std::collections::BTreeMap;
// 連想配列
use std::collections::HashMap;
// 集合
use std::collections::HashSet;
// キュー、スタック
use std::collections::VecDeque;

fn main() {
    input! {
        n: i32,
        a: [[i64;4]; n]
    }
    let mut g = vec![[false; 100]; 100];
    for i in 0..n as usize {
        let x1 = a[i][0];
        let x2 = a[i][1];
        let y1 = a[i][2];
        let y2 = a[i][3];
        for x in x1..x2 {
            for y in y1..y2 {
                let x = x as usize;
                let y = y as usize;
                g[x][y] = true
            }
        }
    }
    let mut ans = 0;
    for i in 0..100 as usize {
        for j in 0..100 as usize {
            if g[i][j] {
                ans += 1
            }
        }
    }
    println!("{}", ans)
}
