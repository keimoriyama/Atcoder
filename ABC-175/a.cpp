#include <iostream>
#include <string>
using namespace std;

int main() {
  char w[3];
  int i,ans,tmp;
  ans = 0;
  tmp = 0;
  for(i = 0; i < 3; i++){
    cin >> w[i];
  }
  for(i = 0; i < 3; i++){
    if(w[i] == 'R'){
      ans++;
      if(tmp < ans){
        tmp = ans;
      }
    }
    else if(w[i] == 'S'){
      ans = 0;
    }
  }
  cout << tmp <<endl;
  return 0;
}
