use itertools::Itertools;
use proconio::input;

fn main() {
    input! {
        n : i32,
        s : [String; n]
    }
    let cond = s
        .into_iter()
        .permutations(2)
        .map(|x| x.concat())
        .any(|x| is_palindrome(&x));

    if cond {
        println!("Yes")
    } else {
        println!("No")
    }
}

fn is_palindrome(s: &str) -> bool {
    let s = s.chars().collect::<Vec<char>>();
    return s == s.iter().rev().copied().collect::<Vec<char>>();
}
