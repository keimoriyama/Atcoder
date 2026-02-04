use itertools::Itertools;
use proconio::input;
use std::collections::VecDeque;

type Edges = Vec<Vec<(usize, usize)>>;

fn main() {
    input! {
        n:usize,m:usize,l:usize,s:usize,t:usize
    };
    let mut edges: Edges = vec![Vec::new(); n];
    for i in 0..m {
        input! {u:usize, v:usize,c:usize};
        edges[u - 1].push((v - 1, c));
    }
    let mut q: VecDeque<(usize, usize, usize)> = VecDeque::new();
    let mut ans: Vec<usize> = Vec::new();
    q.push_back((0, 0, 0));
    while !q.is_empty() {
        if let Some((qi, di, ci)) = q.pop_front() {
            // println!("{:?}", q);
            // println!("{}, {}, {}", qi, di, ci);
            if di == l {
                if s <= ci && ci <= t {
                    ans.push(qi + 1);
                }
                continue;
            } else if di < l {
                for (next, next_cost) in edges[qi].iter() {
                    if ci + next_cost <= t {
                        q.push_back((*next, di + 1, ci + next_cost));
                    }
                }
            }
        }
    }
    ans.sort();
    ans.dedup();
    let out = ans.iter().map(|x| x.to_string()).join(" ");
    println!("{}", out);
}
