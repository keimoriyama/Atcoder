use proconio::input;

fn main() {
    input! {
        n: i64,
        s: String
    }
    let mut flag = false;
    for c in s.chars() {
        if c == '|' {
            flag = !flag;
        } else if flag == true && c == '*' {
            println!("in");
            return;
        } else if flag == false && c == '*' {
            println!("out");
            return;
        }
    }
}
