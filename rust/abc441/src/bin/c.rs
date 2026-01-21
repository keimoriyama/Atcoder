use proconio::input;

fn main() {
    input! {
        n:usize,
        k:usize,
        x:usize,
        mut a:[usize;n]
    };
    a.sort();
    a.reverse();
    //println!("{:?}, n-k: {}", a, n - k);
    let mut ans: usize = 0;
    let mut y: usize = 0;

    for m in 0..n {
        ans += 1;
        if m < (n - k) {
            continue;
        }
        y += a[m];
        //println!("m:{} a[m]:{} y:{} ans:{}", m, a[m], y, ans);
        if y >= x {
            break;
        }
    }
    if y >= x {
        println! {"{}", ans}
    } else {
        println!("-1")
    }
}
