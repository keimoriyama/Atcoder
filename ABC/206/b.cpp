#include <algorithm>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
  long long N;
  cin >> N;
  double n = -1 + sqrt(1 + 8 * N);
  n = n / 2.0;
  n = ceil(n);
  cout << n << endl;
  return 0;
}
