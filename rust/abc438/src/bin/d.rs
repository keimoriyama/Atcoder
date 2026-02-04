use proconio::input;

fn main() {
    input! {
        n: usize,
        a: [i64; n],
        b: [i64; n],
        c: [i64; n],
    };
    // let mut a_sum = vec![0; n];
    // let mut b_sum = vec![0; n];
    // let mut c_sum = vec![0; n];
    // a_sum[0] = a[0];
    // b_sum[0] = b[0];
    // c_sum[0] = c[0];
    // for i in 1..n {
    //     a_sum[i] = a_sum[i - 1] + a[i];
    //     b_sum[i] = b_sum[i - 1] + b[i];
    //     c_sum[i] = c_sum[i - 1] + c[i];
    // }
    // let mut ans = 0;
    // for x in 0..n - 2 {
    //     for y in x + 1..n - 1 {
    //         ans = ans.max(a_sum[x] + (b_sum[y] - b_sum[x]) + (c_sum[n - 1] - c_sum[y]));
    //         //println!("{}, {}, {}", x, y, ans);
    //     }
    // }
    // println!("{}", ans)
    let mut dp: Vec<Vec<i64>> = vec![vec![-1000000000000000010; 4]; n + 1];
    dp[0][0] = 0;
    for i in 0..n {
        dp[i + 1][1] = (dp[i][0].max(dp[i][1])) + a[i];
        dp[i + 1][2] = (dp[i][1].max(dp[i][2])) + b[i];
        dp[i + 1][3] = (dp[i][2].max(dp[i][3])) + c[i]
    }
    println!("{}", dp[n][3])
}
