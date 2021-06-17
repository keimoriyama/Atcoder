#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
  string s;
  cin >> s;
  int ans = 0;
  for (int i = 0; i <= 9999; i++) {
    vector<bool> flag(10);
    int X = i;
    for (int j = 0; j < 4; j++) {
      flag[X % 10] = true;
      X = X / 10;
    }
    bool flag2 = true;
    for (int j = 0; j <= 10; j++) {
      // 確実に含まれていて，Xに存在しない
      if (s[j] == 'o' && !flag[j])
        flag2 = false;
      // 確実に含まれていなくて，Xに存在する
      if (s[j] == 'x' && flag[j])
        flag2 = false;
    }
    ans += flag2;
  }
  cout << ans << endl;
  return 0;
}
