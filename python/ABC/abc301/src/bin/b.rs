use proconio::input;
fn main() {
    input! {
        n : i64,
        t: i64,
        c: [i64;n],
        r: [i64;n]
    };
    let mut color = c.iter();
    let mut ans = 0;
    let mut max_v = 0;
    if color.any(|&x| x == t) {
        for i in 0..n as usize {
            if c[i] == t {
                // println!("{} {} {} {}", c[i], r[i], max_v, t);
                if max_v < r[i] {
                    ans = i;
                    max_v = r[i];
                }
            }
        }
    } else {
        let t = c[0];
        for i in 0..n as usize {
            if c[i] == t {
                if max_v < r[i] {
                    ans = i;
                    max_v = r[i];
                }
            }
        }
    }
    println!("{}", ans + 1);
}
