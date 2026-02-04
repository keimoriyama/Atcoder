use proconio::input;

fn main() {
    let MOD = 998244353;

    input! {
        n:usize,
        m:usize,
        mut a:[i128;n],
        mut b:[i128;m]
    }
    a.sort();
    b.sort();
    let mut r_a = vec![0; n + 1];
    let mut s_a = vec![0; n + 1];
    r_a[0] = 0;
    for i in 0..n {
        r_a[i + 1] = r_a[i] + a[i]
    }
    s_a[n - 1] = a[n - 1];
    for i in (0..n).rev() {
        s_a[i] = s_a[i + 1] + a[i]
    }

    let mut ans = 0;
    for i in 0..m {
        let x = a.partition_point(|&ai| ai < b[i]);
        ans += ((b[i] * (x as i128)) - r_a[x]) % MOD;
        ans += (s_a[x] - (b[i] * ((n - x) as i128))) % MOD;
    }
    println!("{}", ans % MOD);
}
