#include <iostream>
#include <string>
#include <vector>

using namespace std;


int main(int argc, char *argv[])
{
  long N;
  long ans;
  cin >> N;
  vector<long long> a(N);
  for (int n = 0; n < N; n++) {
    cin >> a.at(n);
  }
  for(int i = 0;i < N; i++){
    for(int j = i + 1; j < N ; j++){
      ans += a.at(i) * a.at(j);
    }
  }
  cout << ans % long((1e9+7)) << endl;
  return 0;
}
