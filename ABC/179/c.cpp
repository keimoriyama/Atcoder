#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(int argc, char *argv[])
{
  int N;
  int ans = 0;
  cin >> N;
  for(int A = 1; A < N;A++){
    ans += (N-1)/A;
  }
  cout << ans << endl;
  return 0;
}
