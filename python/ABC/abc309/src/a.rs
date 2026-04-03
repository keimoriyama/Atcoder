use proconio::input;

fn main(){
    input!{
        a: i32,
        b: i32,
    }
    if a %3 == 0{
        println!("No");
        return;
    }
    if a+1 == b{
        println!("Yes");
    }else{
        println!("No");
    }
}
