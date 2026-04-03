use proconio::input;

fn main() {
    input! {
        s: [i32; 8]
    }
    for i in 0..7 {
        if s[i] > s[i + 1] {
            println!("No");
            return;
        }
        let si = s[i];
        if !(100 <= si && si <= 675 && si % 25 == 0) {
            println!("No");
            return;
        }
    }
    println!("Yes");
}
