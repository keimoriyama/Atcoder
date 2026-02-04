use std::convert::TryInto;

use proconio::input;

fn main() {
    input! {
        n:usize
    };
    println!("{}", 2_usize.pow(n.try_into().unwrap()) - 2 * n)
}
