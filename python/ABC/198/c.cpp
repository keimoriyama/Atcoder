#include <algorithm>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
  double R, X, Y;
  cin >> R >> X >> Y;
  double dis = sqrt(X * X + Y * Y);
  double ans = ceil(dis / R);
  if (ans == 1 && dis != R)
    ans++;
  cout << ans << endl;
  return 0;
}
