use std::convert::TryInto;

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
        n: usize
    }
    // if n % 2 != 0 && n % 3 != 0 {
    //     println!("No");
    //     return;
    // }

    let two: usize = 2;
    let three: usize = 3;
    let n_f = n as f64;
    let max_x = (n_f.log(2 as f64) + 10.0) as usize;
    let max_y = (n_f.log(3 as f64) + 10.0) as usize;
    for i in 0..max_x {
        for j in 0..max_y {
            let a = two.pow(i.try_into().unwrap()) * three.pow(j.try_into().unwrap());
            if n == a {
                println!("Yes");
                return;
            }
        }
    }
    println!("No")
}
