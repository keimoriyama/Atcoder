#include <iostream>
#include <string>
#include <vector>

using namespace std;


int main(int argc, char *argv[])
{
  int A, B, c;
  int ans = 0;
  cin >> A >> B;
  c = 1;
  // cout << "A: "<< A << " c: " << c << endl;
  while(c < B){
    c--;
    c += A;
    ans++;
    // cout << "A: "<< A << " c: " << c << endl;
  }
  cout << ans << endl;
  return 0;
}
