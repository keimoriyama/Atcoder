#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
  long long N;
  cin >> N;
  vector<long long> A;
  long long tmp, same = 0;
  int index = 0;
  for (int i = 0; i < N; i++) {
    cin >> tmp;
    A.push_back(tmp);
  }
  sort(A.begin(), A.end());
  long long total = N * (N - 1) / 2;
  long long num = 1;
  for (int i = 0; i < N; i++) {
    if (A[i] != A[i + 1]) {
      total = total - ((num * (num - 1)) / 2);
      num = 1;
    } else {
      num++;
    }
    // cout << total << endl;
  }
  cout << total << endl;
  return 0;
}
