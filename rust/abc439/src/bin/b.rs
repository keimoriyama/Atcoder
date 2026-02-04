use proconio::input;
use std::collections::HashSet;

fn main() {
    input! {mut n:i32};
    let mut calculation_sets: HashSet<i32> = HashSet::new();
    let mut s = 0;
    loop {
        s = 0;
        for i in (0..4).rev() {
            let tmp = n / 10_i32.pow(i) % 10;
            s += tmp.pow(2);
        }
        if calculation_sets.contains(&s) || s == 1 {
            break;
        };
        calculation_sets.insert(s);
        n = s.clone();
    }
    if s == 1 {
        println!("Yes")
    } else {
        println!("No")
    }
}
