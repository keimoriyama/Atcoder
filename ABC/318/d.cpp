#include <bits/stdc++.h>
#include <iostream>
#include <vector>
using namespace std;
#define rep(i, x) for (int i = 0; i < (x); i++)

int main() {
  long long N;
  cin >> N;
  vector g(N, vector(N, 0));
  rep(i, N) {
    for (int j = i + 1; j < N; j++) {
      cin >> g[i][j];
    }
  }
  vector dp(1 << N, 0ll);
  rep(b, (1 << N) - 1) {
    int l = -1;
    rep(i, N) if (!(b >> i & 1)) {
      l = i;
      break;
    }
    rep(i, N) if (!(b >> i & 1)) {
      int nb = b | (1 << l) | (1 << i);
      dp[nb] = max(dp[nb], dp[b] + g[l][i]);
    }
  }
  cout << dp.back() << endl;
  return 0;
}
