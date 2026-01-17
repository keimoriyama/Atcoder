use proconio::input;

fn main() {
    input! {
        n: i32,
        mut a: [i32;n]
    }
    let mut ans = 0;
    // let mut ok = true;
    // while ok {
    //     for i in 0..a.len() {
    //         if a[i] % 2 != 0 {
    //             ok = false
    //         }
    //         a[i] = a[i] / 2;
    //     }
    //     if ok {
    //         ans = ans + 1;
    //     }
    // }
    while a.iter().all(|&x| x % 2 == 0) {
        for x in &mut a {
            *x /= 2
        }
        ans += 1
    }
    println!("{}", ans)
}
