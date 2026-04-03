#include <iostream>
#include <string>
#include <vector>

using namespace std;

int check(int n);

int main(int argc, char *argv[])
{
  int N, tmp = 0, ans, max = -1;
  cin >> N;
  for(int i = 1; i <= N; i++){
    tmp = check(i);
    if(max < tmp){
      max = tmp;
      ans = i;
    }
  }
  cout << ans << endl;
  return 0;
}

int check(int n){
  int a = -1;
  while(n >= 1){
    n /= 2;
    a++;
  }
  if(a == -1)
    a++;
  return a;
}
