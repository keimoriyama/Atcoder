use proconio::input;
// 2分木
// use std::collections::BTreeMap;
// 連想配列
use std::collections::HashMap;
// 集合
// use std::collections::HashSet;
// キュー、スタック
// use std::collections::VecDeque;

fn main() {
    input! {
        s:String
    }
    let chars: Vec<char> = s.chars().clone().collect();
    let length = chars.len();
    let length_map: HashMap<usize, usize> = HashMap::from([
        (1, 0),
        (2, 0),
        (3, 0),
        (4, 1),
        (5, 2),
        (6, 3),
        (7, 4),
        (8, 5),
        (9, 6),
    ]);
    let lim = length - length_map[&length];
    for i in 0..length {
        if i < lim {
            print!("{}", chars[i])
        } else {
            print!("0")
        }
    }
    println!("")
}
