#include <iostream>
#include <string>
#include <math.h>
using namespace std;

int64_t step(int64_t,int64_t,int64_t);

int main() {
  int64_t X, K, D,ans;
  cin >> X >> K >> D;
  int64_t way1,way2;
  while(K > 0){
    way1 = X - D;
    way2 = X + D;
    if(abs(way1) < abs(way2)){
      ans = way1;
    }
    else{
      ans = way2;
    }
    K--;
  }
  cout << ans << endl;
  return 0;
}

/*int64_t step(int64_t x, int64_t k, int64_t d){
  int64_t way1,way2,x1;
  if(k == 0)return x;
  way1 = x - d;
  way2 = x + d;
  if(abs(way1) < abs(way2))
    x1 = way1;
  else
    x1 = way2;
  return step(x1,k-1,d);
}
*/
