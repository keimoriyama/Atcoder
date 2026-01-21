use proconio::input;
fn main() {
    input! {mut s: String};

    let search_string = ["dream", "dreamer", "erase", "eraser"];
    let mut res = "NO";
    loop {
        if s.is_empty() {
            res = "YES";
            break;
        }

        let mut s_sliced = s.clone();
        for search_str in search_string.iter() {
            if s.ends_with(search_str) {
                s_sliced = s[..s.len() - search_str.len()].to_string()
            }
        }
        if s_sliced == s {
            break;
        }

        s = String::from(s_sliced);
    }

    println!("{}", res)
}
