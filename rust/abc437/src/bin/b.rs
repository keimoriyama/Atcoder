use proconio::input;

fn main() {
    input! {
        h:usize,
        w:usize,
        n:usize,
        a: [[usize; w];h],
        b: [usize;n]
    };
    let mut ans = 0;
    for i in 0..h {
        let mut tmp = 0;
        for j in 0..n {
            let bi = b[j];
            tmp += a[i].iter().filter(|&&ai| ai == bi).count();
        }
        ans = ans.max(tmp)
    }
    println!("{}", ans)
}
