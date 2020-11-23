#include <iostream>
#include <iomanip>
#include <string>
#include <vector>

using namespace std;

int main(int argc, char *argv[])
{
  double sx, sy, gx, gy;
  double ans;
  cin >> sx >> sy >> gx >> gy;
  ans = (sx * gy + gx * sy) / (sy + gy);
  cout << fixed << setprecision(10) << ans << endl;
  return 0;
}
