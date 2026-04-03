#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
  int N;
  bool flag = true;
  cin >> N;
  if (N == 0)
    cout << "Yes" << endl;
  else {
    while (N % 10 == 0)
      N = N / 10;
    string n = to_string(N);
    // cout << n << endl;
    for (int i = 0; i < (int)n.size() / 2; i++) {
      // cout << i << " " << n.size() - i - 1 << endl;
      if (n[i] != n[n.size() - i - 1]) {
        flag = false;
        break;
      }
    }
    if (flag)
      cout << "Yes" << endl;
    else
      cout << "No" << endl;
  }
  return 0;
}
