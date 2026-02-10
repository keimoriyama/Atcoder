use proconio::input;

fn main() {
    input! {mut n:usize};

    let mut m = vec![vec![-1; n]; n];
    let mut k = 1;
    let mut r = 0;
    let mut c = (n - 1) / 2;
    m[r][c] = k;
    k += 1;
    for _ in 0..(n.pow(2) - 1) {
        let prev_r = r;
        let prev_c = c;
        // if r <= 0 {
        //     r = n - 1;
        // } else {
        //     r = (r - 1) % n
        // };
        r = (r + n - 1) % n;
        c = (c + 1) % n;
        // println!("{} {} {} {}", r, c, m[r][c], k);
        if m[r][c] == -1 {
            m[r][c] = k;
        } else {
            r = (prev_r + 1) % n;
            m[r][prev_c] = k;
            c = prev_c;
        }
        k += 1;
    }
    for mi in m.iter() {
        println!(
            "{}",
            mi.iter()
                .map(|x| x.to_string())
                .collect::<Vec<String>>()
                .join(" ")
        )
    }
}
