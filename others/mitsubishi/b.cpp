#include <iostream>
#include <string>
#include <math.h>


using namespace std;


int main(int argc, char *argv[])
{
  int N, i;
  cin >> N;
  int ans = -1;
  for(i = 1; i <= N; i++){
    if(N == floor(i * 1.08))
      ans = i;
  }
  if(ans != -1)
    cout << ans << endl;
  else
    cout << ":(" << endl;
  return 0;
}
