use proconio::input;

fn main() {
    input! {
        n: i32,
        a:[i32;7*n]
    }
    for i in 0..n as usize {
        let mut ans = 0;
        for j in 0..7 as usize {
            ans = ans + a[i * 7 + j]
        }
        print!("{} ", ans);
    }
    println!()
}
