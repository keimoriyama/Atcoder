#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;
vector<vector<int>> a;

int main() {
  int N;
  bool ans = true;
  cin >> N;
  vector<int> a(N);
  for (int i = 0; i < N; i++)
    cin >> a[i];
  sort(a.begin(), a.end());
  for (int i = 0; i < N; i++) {
    if (a[i] != i + 1)
      ans = false;
  }
  if (ans)
    cout << "Yes" << endl;
  else
    cout << "No" << endl;
  return 0;
}
