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
    }
    let mut s: Vec<Vec<char>> = vec![];
    for _i in 0..n {
        input! {
            si:String
        }
        s.push(si.chars().collect())
    }
    // println!("{:?}", s);
    for i in 0..n {
        for j in 0..m {
            // println!("{} {}", i, j);
            let res = eval(s.clone(), i, j);
            if res {
                println!("{} {}", i + 1, j + 1);
            }
        }
    }
}

fn eval(map: Vec<Vec<char>>, i: usize, j: usize) -> bool {
    let mut ok = true;
    if i + 9 > map.len() || j + 9 > map[i].len() {
        return false;
    }
    // 左上の判定
    for ri in 0..4 {
        for rj in 0..4 {
            if ri == 3 || rj == 3 {
                if map[i + ri][j + rj] != '.' {
                    ok = false
                }
            } else {
                if map[i + ri][j + rj] != '#' {
                    ok = false
                }
            }
        }
    }
    // 右下の判定
    for ri in i + 5..i + 9 {
        for rj in j + 5..j + 9 {
            // println!("  {} {}", ri, rj);
            // if i == 0 && j == 0 {
            //     println!("{} {} {}", ri, rj, map[ri][rj]);
            // }

            if ri == i + 5 || rj == j + 5 {
                if map[ri][rj] != '.' {
                    ok = false;
                }
            } else {
                if map[ri][rj] != '#' {
                    ok = false;
                }
            }
        }
    }
    // println!("{}", ok);
    return ok;
}
