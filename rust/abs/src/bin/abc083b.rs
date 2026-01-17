use proconio::input;

fn digit_sum(mut x: i32) -> i32 {
    let mut sum = 0;
    while x > 0 {
        sum += x % 10;
        x /= 10;
    }
    sum
}

fn main() {
    input! {
    n: i32,
    a: i32,
    b:i32
    }
    // let mut ans = 0;
    // for i in 1..=n {
    //     let mut s = 0;
    //     for j in 0..=3 {
    //         s += i / (10_i32.pow(j)) % 10;
    //     }
    //     if a <= s && s <= b {
    //         ans += i;
    //     }
    // }
    let ans: i32 = (1..=n)
        .filter(|&i| {
            let s = digit_sum(i);
            a <= s && s <= b
        })
        .sum();
    println!("{}", ans)
}
