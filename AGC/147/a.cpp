#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

int main() {
  int N;
  int i,j,out;
  out = 0;
  cin >> N;
  double a[N],ans;
  for(i = 0; i < N; i++){
    cin >> a[i];
  }
  for(i = 0; i < N; i++){
    for(j = i+1; j < N; j++){
      ans = a[i]*a[j];
      if(floor(ans) == ans){
      // 値の近いほぼ１の少数をかけると丸め誤差が生じる
      cout << fixed << setprecision(15) <<a[i] << "*" << a[j] << "=" << ans << endl;
        out+= 1;
      }
    }
  }
  cout << out << endl;
  return 0;
}
