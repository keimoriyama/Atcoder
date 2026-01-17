use proconio::input;
use proconio::marker::Chars;
fn main() {
    input! {
        s: Chars,
    }
    let mut c = 0;
    for si in s {
        if si == '1' {
            c = c + 1;
        }
    }
    println!("{}", c)
}
