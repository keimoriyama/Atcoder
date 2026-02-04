use proconio::input;
use std::collections::HashMap;
fn main() {
    input! {
        n:usize,
        mut a:[usize;n]
    }
    fn solve(a: &Vec<usize>) -> usize {
        let mut t: HashMap<usize, usize> = HashMap::new();
        let mut s: HashMap<usize, usize> = HashMap::new();
        let mut ans = 0;
        for &ai in a.iter() {
            if ai % 3 == 0 {
                //t[&(ai / 3)] += 1;
                let k = ai / 3;
                *t.entry(k).or_insert(0) += 1;
            }
            if ai % 7 == 0 {
                let k = ai / 7;
                *s.entry(k).or_insert(0) += 1;
            }
            if ai % 5 == 0 {
                let k = ai / 5;
                if t.contains_key(&k) && s.contains_key(&k) {
                    ans += t[&(ai / 5)] * s[&(ai / 5)];
                }
            }
        }
        ans
    }
    let mut ans = solve(&a);
    a.reverse();
    ans += solve(&a);
    println!("{}", ans)
}
