#include <iostream>
#include <string>
#include <math.h>
using namespace std;

int main(int argc, char* argv[]) {
  int K, result;
  result = 1;
  int i = 1;
  bool flag = false;
  cin >> K;
  int64_t num = 7;
  while(true){
    if((K % 2) == 0 || num < 0){
      break;
    }
    if((num % K) == 0){
      flag = true;
      break;
    }
    num = num + 7 * pow(10,i);
    cout << num << endl;
    result = result + 1;
    i = i + 1;
  }
  if(flag){
    cout << result << endl;
  }
  else{
    cout << -1 << endl;
  }
  return 0;
}
