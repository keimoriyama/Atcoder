use proconio::input;

fn main() {
    input! {
        n:usize,
        a:[usize;n]
    };
    let mut stack: Vec<usize> = Vec::new();
    for &ai in a.iter() {
        stack.push(ai);
        let mut stack_len = stack.len();
        if stack_len < 4 {
            continue;
        }
        //println!("{:?}, {}", stack, stack_len);
        while stack_len >= 4
            && stack[stack_len - 4] == stack[stack_len - 3]
            && stack[stack_len - 3] == stack[stack_len - 2]
            && stack[stack_len - 2] == stack[stack_len - 1]
        {
            for _ in 0..4 {
                stack.pop();
            }
            stack_len = stack.len();
        }
    }
    println!("{}", stack.len());
}
