use proconio::input;
use proconio::marker::Chars;
use std::collections::HashMap;
use std::collections::VecDeque;
fn main() {
    input! {
        h:usize,
        w:usize,
        s:[Chars; h]
    };
    let mut tele_map: HashMap<char, Vec<(usize, usize)>> = HashMap::new();
    let mut seen: HashMap<char, bool> = HashMap::new();

    for i in 0..h {
        for j in 0..w {
            let sij = s[i][j];
            if sij != '.' && sij != '#' {
                tele_map.entry(sij).or_insert_with(Vec::new).push((j, i));
                seen.insert(sij, false);
            }
        }
    }
    //println!("{:?}", tele_map);
    let mut queue: VecDeque<(usize, usize, usize)> = VecDeque::new();
    let mut flag = vec![vec![false; w]; h];
    queue.push_back((0, 0, 0));
    flag[0][0] = true;
    let mut ans = 0;
    let dx: Vec<isize> = vec![0, 0, 1, -1];
    let dy: Vec<isize> = vec![1, -1, 0, 0];
    let mut current_masu = s[0][0];
    while let Some(xy) = queue.pop_front() {
        let x = xy.0;
        let y = xy.1;
        let d = xy.2;
        //println!("{} {}", x, y);
        if x == w - 1 && y == h - 1 {
            ans = d;
            break;
        }
        current_masu = s[y][x];

        for i in 0..4 {
            let n_x = x as isize + dx[i];
            let n_y = y as isize + dy[i];
            if n_x < 0 || n_y < 0 || n_x >= w as isize || n_y >= h as isize {
                continue;
            }
            let (n_x, n_y) = (n_x as usize, n_y as usize);

            if flag[n_y][n_x] || s[n_y][n_x] == '#' {
                continue;
            }
            flag[n_y][n_x] = true;
            queue.push_back((n_x, n_y, d + 1));
        }

        if current_masu != '.' && !seen[&current_masu] {
            let n_p_candidate = tele_map[&current_masu].clone();
            seen.insert(current_masu, true);
            for np in n_p_candidate.iter() {
                if flag[np.1][np.0] {
                    continue;
                }
                flag[np.1][np.0] = true;
                queue.push_back((np.0, np.1, d + 1));
            }
        }
    }
    if ans == 0 {
        println!("-1")
    } else {
        println!("{}", ans)
    }
}
