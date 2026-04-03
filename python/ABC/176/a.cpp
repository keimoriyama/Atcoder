#include <iostream>
#include <string>

using namespace std;

int
main() {
  int N, X, T;
  int n,ans;
  cin >> N >> X >> T;
  n = N / X;
  if(N % X > 0)
    n++;
  ans = n * T;
  cout << ans << endl;
  return 0;
}
