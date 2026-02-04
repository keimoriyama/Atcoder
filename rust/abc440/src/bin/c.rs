use proconio::input;

fn main() {
    input! {
        t:usize
    }
    for _i in 0..t {
        input! {
            n:usize,
            w:usize,
            c:[usize;n]
        }
        let mut sum_costs = vec![0; 2 * w];
        for i in 0..n {
            sum_costs[i % (2 * w)] += c[i];
        }
        let mut current: usize = sum_costs[0..w].iter().sum();
        let mut ans = current;
        //println!("{:?}", sum_costs);
        for x in 0..2 * w {
            current += sum_costs[(x + w) % (2 * w)];
            current -= sum_costs[x];
            if ans > current {
                ans = current;
            }
        }
        println!("{}", ans)
    }
}
