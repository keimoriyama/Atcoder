#include <iostream>
#include <string>
#include <vector>

using namespace std;


int main(int argc, char *argv[])
{
  int N;
  int tai = 0, ans = 1e9;
  cin >> N;
  N++;
  vector<int> X(N);
  for(int i = 1; i < N; i++)
    cin >> X[i];

  for(int i = 1; i < 100; i++){
    for(int j = 1; j < N; j++){
      tai += (X[j] - i)*(X[j] - i);
    }
    /*
    cout << "i : " << i << endl;
    cout << "tai: " << tai << endl;
    cout << "ans: " << ans << endl;
    */
    ans = min(ans, tai);
    tai = 0;
  }
  cout << ans << endl;
  return 0;
}
