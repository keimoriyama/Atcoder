use proconio::input;

fn main() {
    input! {
        n:usize,
        a: [String;n]
    }
    let mut ans: Vec<Vec<char>> = vec![vec!['a'; n]; n];
    for i in 0..n as usize {
        for j in 0..n as usize {
            if i == 0 || j == 0 || i == n - 1 || j == n - 1 {
                if i == 0 && j < n - 1 {
                    ans[i][j + 1] = a[i].chars().nth(j).unwrap();
                } else if i < n - 1 && j == n - 1 {
                    ans[i + 1][j] = a[i].chars().nth(j).unwrap();
                } else if i == n - 1 && j > 0 {
                    ans[i][j - 1] = a[i].chars().nth(j).unwrap();
                } else if i > 0 && j == 0 {
                    ans[i - 1][j] = a[i].chars().nth(j).unwrap();
                }
            } else {
                ans[i][j] = a[i].chars().nth(j).unwrap();
            }
        }
    }
    for i in 0..n as usize {
        for j in 0..n as usize {
            print!("{}", ans[i][j]);
        }
        println!();
    }
}
