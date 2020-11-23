#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;


int main(int argc, char *argv[])
{
  int N;
  int ans = 1e9,bit = 0,tmp;
  int res1 = 0, res2 = 0;
  cin >> N;
  vector<int> meat(N);
  for (int n = 0; n < N; n++) {
    cin >> meat[n];
  }
  while((bit & (1 << (N+1))) == 0){
    for (int i = 0; i < N; i++) {
      if(bit & (1 << i))
        res1 += meat[i];
      else
        res2 += meat[i];
    }
    tmp = max(res1,res2);
    bit++;
    res1 = 0;res2 = 0;
    if(ans >= tmp)
      ans = tmp;
  }
  cout << ans << endl;
  return 0;
}
