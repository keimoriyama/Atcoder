#include <iostream>
#include <string>
#include <vector>

using namespace std;


int main(int argc, char *argv[])
{
  int N, M, C;
  int ans = 0, tmp = 0;
  cin >> N >> M >> C;
  vector<int> B(M);
  vector<vector<int> > A(N, vector<int>(M));
  for(int i = 0; i < M; i++)
    cin >> B[i];
  for(int i = 0; i < N; i++){
    for(int j = 0; j < M; j++){
      cin >> A[i][j];
    }
  }
  for(int i = 0; i < N; i++){
    for(int j = 0; j < M; j++){
      tmp = tmp + B[j] * A[i][j];
    }
    if((tmp+C) > 0)
      ans++;
    tmp = 0;
  }
  cout << ans << endl;
  return 0;
}
