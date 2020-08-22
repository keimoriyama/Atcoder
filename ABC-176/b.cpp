#include <iostream>
#include <string>
#include <vector>
#include <boost/multiprecision/cpp_int.hpp>

using namespace std;
using namespace boost::multiprecision;

int main() {
  cpp_int N,n;
  int keta,sum;
  cin >> N;
  keta = 0;
  sum = 0;
  n = N;
  while(n != 0){
    n = n / 10;
    keta++;
  }
  vector<int> a(keta);
  for (int n = 0; n < keta; n++) {
    a[n] = int(N % 10);
    N /= 10;
  }
  for (int n = 0; n < keta; n++) {
    sum += a[n];
  }
  if(sum % 9 == 0){
    cout << "Yes" << endl;
  }
  else{
    cout << "No" << endl;
  }
  return 0;
}
