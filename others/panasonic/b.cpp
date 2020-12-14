#include <iostream>
#include <string>
#include <vector>

using namespace std;


int main(int argc, char *argv[])
{
  long long H, W;
  cin >> H >> W;
  long long ans = 0;

  if(H == 1 | W == 1){
    ans = 1;
  }else{
    ans = (H * W + 1)/2;
  }
  cout << ans << endl;
  return 0;
}
