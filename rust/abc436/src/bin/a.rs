use proconio::input;

fn main() {
    input! {
        n:usize,
        s:String
    };
    // let o_num = n - s.len();
    // for _ in 0..o_num {
    //     print!("o")
    // }
    // println!("{}", s);
    println!("{}{}", "o".repeat(n.saturating_sub(s.len())), s);
}
