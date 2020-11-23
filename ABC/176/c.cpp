#include <iostream>
#include <string>

using namespace std;

int main() {
  int N;
  cin >> N;
  int a[N];
  long cnt;
  cnt = 0;
  for (int n = 0; n < N; n++) {
    cin >> a[n];
  }
  for (int n = 1; n < N; n++) {
    while(a[n-1] > a[n]){
      a[n] += 1;
      cnt+=1;
    }
  }
  cout << cnt << endl;
  return 0;
}
