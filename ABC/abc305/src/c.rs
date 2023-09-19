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
    let mut min_x: usize = h;
    let mut min_y: usize = w;
    let mut max_x: usize = 0;
    let mut max_y: usize = 0;

    for i in 0..h {
        let si: Vec<char> = s[i].chars().collect();
        for j in 0..w {
            if si[j] == '#' {
                if min_x > j {
                    min_x = j
                }
                if min_y > i {
                    min_y = i
                }
                if max_x < j {
                    max_x = j
                }
                if max_y < i {
                    max_y = i
                }
            }
        }
    }
    // println!("{} {} {} {}", min_x, min_y, max_x, max_y);
    for i in min_y..max_y + 1 {
        let si: Vec<char> = s[i].chars().collect();
        for j in min_x..max_x + 1 {
            if si[j] == '.' {
                println!("{} {}", i + 1, j + 1)
            }
        }
    }
}
