use proconio::input;

fn main() {
    input! {
        p: i32,
        q:i32,
        x:i32,
        y:i32
    }
    if (p <= x && x < p + 100) && (q <= y && y < q + 100) {
        println!("Yes")
    } else {
        println!("No")
    }
}
