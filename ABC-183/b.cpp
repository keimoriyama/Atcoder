#include <iostream>
#include <string>
#include <vector>

using namespace std;


int main(int argc, char *argv[])
{
  int sx, sy, gx, gy;
  long long mid, left, right;
  long long grad, seppen, y;
  cin >> sx >> sy >> gx >> gy;
  left = sx;
  right = gx;
  while(left <= right){
    mid = (left + right)/2;
    grad = gy/(gx-mid);
    seppen = -(grad * mid);
    y = (grad * gx) + seppen;
    if(y == gy){
      break;
    }
    if(y < gy){
      right = mid;
    }
    else{
      left = mid;
    }
  }
  cout << y << endl;
  return 0;
}
