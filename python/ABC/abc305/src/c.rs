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
        h:usize,
        w:usize,
        s:[String;h]
    }
    let mut min_x: usize = 1 << 30;
    let mut min_y: usize = 1 << 30;
    let mut max_x: usize = 0;
    let mut max_y: usize = 0;

    for i in 0..h {
        let si: Vec<char> = s[i].chars().collect();
        for j in 0..w {
            if si[j] == '#' {
                min_x = min_x.min(j);
                min_y = min_y.min(i);
                max_x = max_x.max(j);
                max_y = max_y.max(i);
            }
        }
    }
    for i in min_y..=max_y {
        let si: Vec<char> = s[i].chars().collect();
        for j in min_x..=max_x {
            if si[j] == '.' {
                println!("{} {}", i + 1, j + 1);
                return;
            }
        }
    }
}
