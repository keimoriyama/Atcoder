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
    }
    let mut fs = vec![];
    for i in 0..n {
        input! {
            fi:usize,
            si:usize,
        }
        fs.push((fi, si, i))
    }
    let max_fs = fs.iter().max_by(|a, b| a.1.cmp(&b.1)).unwrap();
    // println!("{:?}", fs.iter().max_by(|a, b| a.1.cmp(&b.1)).unwrap());
    let mut ans = 0;
    for i in 0..n {
        let fsi = fs[i];
        if max_fs.2 == fsi.2 {
            continue;
        }
        if fsi.0 == max_fs.0 {
            if ans <= max_fs.1 + (fsi.1 / 2) {
                ans = max_fs.1 + (fsi.1 / 2)
            }
        } else {
            if ans <= max_fs.1 + fsi.1 {
                ans = max_fs.1 + fsi.1
            }
        }
    }
    println!("{}", ans)
}
