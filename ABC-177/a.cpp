#include <iostream>
#include <string>

using namespace std;


int main()
{
  uint64_t D, T, S;
  int time = 0;
  cin >> D >> T >> S;
  time = D / S;
  cout << time << endl;
  if(time <= T)
    cout << "Yes" << endl;
  else
    cout << "No" << endl;
  return 0;
}
