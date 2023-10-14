use std::convert::TryInto;

use proconio::input;
// 2分木
// use std::collections::BTreeMap;
// 連想配列
// use std::collections::HashMap;
// 集合
// use std::collections::HashSet;
// キュー、スタック
use std::collections::VecDeque;

fn main() {
    input! {
        n:isize,
        d:isize,
        xy: [[isize;2];n]
    }
    let mut g = vec![vec![false; n.try_into().unwrap()]; n.try_into().unwrap()];
    for i in 0..n as usize {
        for j in 0..n as usize {
            if i == j {
                continue;
            }
            let xi = xy[i][0];
            let yi = xy[i][1];
            let xj = xy[j][0];
            let yj = xy[j][1];
            let dis2 = (xi - xj).pow(2) + (yi - yj).pow(2);
            if dis2 <= d.pow(2) {
                g[i][j] = true;
            }
        }
    }
    let mut q = VecDeque::new();
    let mut ans = vec![false; n.try_into().unwrap()];
    ans[0] = true;
    q.push_back(0);
    while !q.is_empty() {
        let qi: usize = q.pop_front().unwrap();
        for i in 0..n as usize {
            if g[qi][i] && !ans[i] {
                q.push_back(i);
                ans[i] = true;
            }
        }
    }
    for i in 0..n as usize {
        println!("{}", if ans[i] { "Yes" } else { "No" })
    }
}
