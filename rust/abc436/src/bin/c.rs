use proconio::input;
use std::collections::HashSet;
fn main() {
    input! {
        n:usize,
        m:usize,
        rc: [ [usize;2];m]
    };
    let mut points: HashSet<(usize, usize)> = HashSet::new();
    let mut ans = 0;
    let dxy = vec![vec![0, 0], vec![0, 1], vec![1, 0], vec![1, 1]];

    for i in 0..m {
        let r = rc[i][0] - 1;
        let c = rc[i][1] - 1;
        let mut ok = true;
        for dxyi in dxy.iter() {
            let dx = dxyi[0];
            let dy = dxyi[1];
            ok = ok & (!points.contains(&(r + dx, c + dy)));
        }
        if ok {
            ans += 1;
            for dxyi in dxy.iter() {
                let dx = dxyi[0];
                let dy = dxyi[1];
                points.insert((r + dx, c + dy));
            }
        }
    }
    println!("{}", ans);
}
