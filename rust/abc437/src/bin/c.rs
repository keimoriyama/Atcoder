use itertools::Itertools;
use proconio::input;

fn main() {
    input! {t:usize};
    for _ in 0..t {
        input! {
            n : usize,
            wp: [[usize;2];n]
        }
        let wp_sorted: Vec<&Vec<usize>> = wp
            .iter()
            .sorted_by(|wpi, wpj| (wpi[0] + wpi[1]).cmp(&(wpj[0] + wpj[1])))
            .collect();
        let p_sum: usize = wp.iter().map(|wpi| wpi[1]).sum();

        let mut res = 0;
        for (i, wpi) in wp_sorted.iter().enumerate() {
            res += wpi[0] + wpi[1];
            if res > p_sum {
                println!("{}", i);
                break;
            }
        }
    }
}
