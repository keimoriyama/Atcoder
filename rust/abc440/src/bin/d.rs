use itertools::Itertools;
use proconio::input;

fn main() {
    input! {
            n:usize,
            q:usize,
    mut  a: [usize;n]
    };
    a.sort();
    println!("{:?}", a);
    for _ in 0..q {
        input! {x:usize,y:usize};
        let si = a.partition_point(|&ai| ai < x);
    }
}
