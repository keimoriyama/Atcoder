use proconio::input;
use std::collections::HashMap;

fn main() {
    input! {
        n: i32,
        m: i32,
        c: [String; n],
        d: [String; m],
        p: [i32; m+1],
    }
    let mut c2p = HashMap::new();
    for i in 0..m as usize {
        c2p.insert(d[i].clone(), p[i + 1]);
    }
    // for (key, value) in c2p.iter() {
    //     println!("{} => {}", key, value);
    // }

    let mut ans = 0;
    for i in 0..n as usize {
        match c2p.get(&c[i]) {
            Some(price) => ans += price,
            None => ans += p[0],
        }
        // println!("{}", ans)
    }
    println!("{}", ans)
}
