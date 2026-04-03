#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;


int main(int argc, char *argv[])
{
  int N;
  int A = 0, B = 0;
  bool flag = false;
  cin >> N;
  vector<int> a(N);
  for(int i = 0; i < N; i++)
    cin >> a[i];
  sort(a.begin(), a.end());
  for(int i = N - 1; i >= 0; i--){
    if(!flag)
      A += a[i];
    else if(flag)
      B += a[i];
    flag = !flag;
  }
  cout << A - B << endl;
  return 0;
}
