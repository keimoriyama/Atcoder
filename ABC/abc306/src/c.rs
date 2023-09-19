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
        n:usize,
        a: [usize;3*n]
    }
    let mut count: Vec<usize> = vec![0; n + 1];
    let mut idx: Vec<usize> = vec![0; n + 1];
    let mut map: HashMap<usize, usize> = HashMap::new();
    for i in 0..3 * n {
        let ai = a[i];
        count[ai] += 1;
        if count[ai] == 2 {
            idx[ai] = i;
            map.insert(i, ai);
        }
    }
    idx.sort();
    // println!("{:?}", idx);
    // println!("{:?}", map);
    for i in idx.iter() {
        if map.contains_key(i) {
            print!("{} ", map[i]);
        }
    }
}
