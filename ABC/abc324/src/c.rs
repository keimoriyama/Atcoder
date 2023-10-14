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

fn calc(mut s: Vec<char>, mut t: Vec<char>, reverse: bool) -> usize {
    if reverse {
        s.reverse();
        t.reverse();
    }
    for i in 0..t.len() {
        if i >= s.len() {
            return s.len();
        }
        if s[i] != t[i] {
            return i;
        }
    }
    return t.len();
}

fn main() {
    input! {
        n: usize,
        t: Chars,
        s: [Chars;n]
    }
    let mut a = Vec::new();
    for i in 0..n {
        a.push(calc(s[i].clone(), t.clone(), false));
    }
    let mut b = Vec::new();
    for i in 0..n {
        b.push(calc(s[i].clone(), t.clone(), true));
    }
    let mut ans: Vec<usize> = Vec::new();
    for i in 0..n {
        let si = s[i].clone();
        let mut flag = false;
        if a[i] == si.len() && si.len() == t.len() {
            flag = true
        } else if a[i] + b[i] >= si.len() && si.len() + 1 == t.len() {
            flag = true
        } else if a[i] + b[i] >= si.len() - 1 && si.len() - 1 == t.len() {
            flag = true
        } else if a[i] + b[i] == si.len() - 1 && si.len() == t.len() {
            flag = true
        }
        if flag {
            ans.push(i + 1)
        }
    }
    println!("{}", ans.len());
    for i in 0..ans.len() {
        print!("{} ", ans[i]);
    }
    println!()
}
