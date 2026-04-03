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
        s:String,
        t:String
    }
    let s: Vec<_> = s.chars().collect();
    let t: Vec<_> = t.chars().collect();
    let mut ok = true;
    for i in 0..n {
        let si = s[i];
        let ti = t[i];
        if si == ti {
            continue;
        }
        if (si == '1' && ti == 'l') || (si == 'l' && ti == '1') {
            continue;
        }
        // println!("{} {}", si, ti);
        if (si == '0' && ti == 'o') || (si == 'o' && ti == '0') {
            continue;
        }
        ok = false;
    }
    if ok {
        println!("Yes")
    } else {
        println!("No")
    }
}
