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
        p:char,
        q:char
    }
    let distance = HashMap::from([
        ('A', 0),
        ('B', 3),
        ('C', 4),
        ('D', 8),
        ('E', 9),
        ('F', 14),
        ('G', 23),
    ]);
    let dis_p: i64 = distance[&p];
    let dis_q: i64 = distance[&q];
    println!("{}", (dis_p - dis_q).abs());
}
