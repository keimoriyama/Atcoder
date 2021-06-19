#include <algorithm>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
  int N;
  cin >> N;
  int p = floor(N * 1.08);
  // cout << p << endl;
  if (p < 206)
    cout << "Yay!" << endl;
  else if (p == 206)
    cout << "so-so" << endl;
  else
    cout << ":(" << endl;
  return 0;
}
