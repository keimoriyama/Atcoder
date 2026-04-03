use proconio::input;
use proconio::marker::Chars;
// 2分木
// use std::collections::BTreeMap;
// 連想配列
// use std::collections::HashMap;
// 集合
// use std::collections::HashSet;
// キュー、スタック
// use std::collections::VecDeque;

fn check(s: Vec<char>, t: Vec<char>) -> bool {
    if s.len() > t.len() {
        return check(t, s);
    }
    if s.len() < t.len() - 1 {
        return false;
    }
    let mut i = 0;
    let mut j = 0;
    let mut d = 0;
    while i < s.len() {
        if s[i] == t[j] {
            i += 1;
            j += 1;
        } else {
            d += 1;
            if d > 1 {
                return false;
            }
            if s.len() == t.len() {
                i += 1
            }
            j += 1
        }
    }
    return true;
}

fn main() {
    input! {
        n: usize,
        mut t: Chars,
    }
    let mut ans = Vec::new();
    for i in 0..n {
        input! {
            s: Chars,
        }
        if check(s.clone(), t.clone()) {
            ans.push(i + 1);
        }
    }
    println!("{}", ans.len());
    for i in 0..ans.len() {
        print!("{} ", ans[i]);
    }
    println!()
}
