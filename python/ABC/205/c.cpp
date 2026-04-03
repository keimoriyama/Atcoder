#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
 
using namespace std;
 
int main() {
  long long a, b, c;
  bool a_flag = false, b_flag = false;
  cin >> a >> b >> c;
  if(c%2 == 0&& a<0){
      a = -a;
      a_flag = true;
  }
  if(c%2 == 0&& b<0){
      b = -b;
      b_flag = true;
  }
  if(a == b)
      cout << "=" << endl;
  if(a > b){
      if(!a_flag && b_flag && (a<b))
          cout << "<" << endl;
      else
          cout << ">" << endl;
  }
  if(a < b){
      if(!b_flag && a_flag && (a>b))
          cout << ">" << endl;
      else
          cout << "<" << endl;
  }
  return 0;
}
