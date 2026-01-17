use proconio::input;
fn main() {
    input! {
        a: i32,
        b: i32
    };
    let seki = a * b;
    if seki % 2 == 0 {
        println!("Even")
    } else {
        println!("Odd")
    }
}
