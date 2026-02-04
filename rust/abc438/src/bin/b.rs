use proconio::input;

fn main() {
    input! {
        n:usize,
        m:usize,
        s: String,
        t:String,
    };
    let s_digits: Vec<u32> = s.chars().map(|c| c.to_digit(10).unwrap()).collect();
    let t_digits: Vec<u32> = t.chars().map(|c| c.to_digit(10).unwrap()).collect();
    let mut ans = u32::MAX;
    // for i in 0..(n - m + 1) {
    //     let s_sliced = &s_digits[i..(i + m)];
    //     let mut t_copy = t_digits.to_vec();
    //     let mut tmp_ans = 0;
    //     for j in 0..m {
    //         while s_sliced[j] != t_copy[j] {
    //             t_copy[j] = (t_copy[j] + 1) % 10;
    //             tmp_ans += 1;
    //         }
    //     }
    //     if ans > tmp_ans || ans == -1 {
    //         ans = tmp_ans;
    //     }
    // }
    for i in 0..=n - m {
        let mut tmp_ans = 0;
        for j in 0..m {
            tmp_ans += (s_digits[i + j] + 10 - t_digits[j]) % 10
        }
        if ans > tmp_ans {
            ans = tmp_ans;
        }
    }
    println!("{}", ans);
}
