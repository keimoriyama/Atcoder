#include <iostream>
#include <string>
#include <vector>

using namespace std;


int main(int argc, char *argv[])
{
  int N, K, x_A, x_B;
  int ans = 0;
  cin >> N >> K;
  vector<int> x(N);
  for(int i = 0; i < N; i++)
    cin >> x[i];
  for(int i = 0; i < N; i++){
    x_A = x[i];
    x_B = K - x[i];
    //cout << x_A << " " << x_B << endl;
    if(x_A <= x_B){
      ans += x_A * 2;
    }
    else if(x_A > x_B){
      ans += x_B * 2;
    }
  }
  cout << ans << endl;
  return 0;
}
