use itertools::Itertools;
use proconio::input;
use proconio::marker::Chars;
fn main() {
    input! {
        n: i32,
        m:i32,
        s: Chars,
        t: Chars,
        q:i32,
        w: [Chars;q]
    };
    let t_only: Vec<char> = t
        .iter()
        .filter(|&ti| !s.contains(ti))
        .map(|c| *c)
        .collect_vec();
    let s_only = s
        .iter()
        .filter(|&si| !t.contains(si))
        .map(|c| *c)
        .collect_vec();

    for wi in w.iter() {
        let taka = wi.iter().any(|wi| t_only.contains(wi));
        let ao = wi.iter().any(|wi| s_only.contains(wi));
        if taka && !ao {
            println!("Aoki")
        } else if !taka && ao {
            println!("Takahashi")
        } else {
            println!("Unknown")
        }
    }
    // for wi in w.iter() {
    //     let mut ok = false;
    //     for wij in wi.iter() {
    //         if t.contains(wij) && s.contains(wij) {
    //             continue;
    //         } else if t.contains(wij) && !s.contains(wij) {
    //             //println!("{:?} {}", t, wij);
    //             println!("Aoki");
    //             ok = true;
    //         } else if !t.contains(wij) && s.contains(wij) {
    //             //println!("{:?} {}", s, wij);
    //             println!("Takahashi");
    //             ok = true;
    //         }
    //         if ok {
    //             break;
    //         }
    //     }
    //     if !ok {
    //         println!("Unknown");
    //     }
    // }
}
