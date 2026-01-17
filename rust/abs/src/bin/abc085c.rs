use proconio::input;

fn main() {
    input! {
        n: i64,
        y: i64
    }
    let mut ok = false;
    for i in 0..=n {
        for j in 0..=n {
            let k = n - i - j;
            if k < 0 {
                continue;
            }
            if y == (10000 * i + 5000 * j + 1000 * k) {
                println!("{} {} {}", i, j, k);
                ok = true
            }
            if ok {
                break;
            }
        }
        if ok {
            break;
        }
    }
    if !ok {
        println!("-1 -1 -1")
    }
}
