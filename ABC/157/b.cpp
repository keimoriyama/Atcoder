#include <iostream>
#include <string>
#include <vector>

using namespace std;


int main(int argc, char *argv[])
{
  vector<vector<int> > bingo(3, vector<int>(3,0));
  vector<vector<bool> > check(3, vector<bool>(3,0));
  int N;
  bool ans = false;
  for(int i = 0; i < 3; i++){
    for(int j = 0; j < 3; j++){
      cin >> bingo[i][j];
    }
  }
  cin >> N;
  vector<int> b(N);
  for(int i = 0; i < N; i++){
    cin >> b[i];
  }
  for(int i = 0; i < N; i++){
    for(int j = 0; j < 3; j++){
      for(int k = 0; k < 3; k++){
        if(b[i] == bingo[j][k]){
          check[j][k] = true;
        }
      }
    }
  }
  for(int i = 0; i < 3; i++){
    if(check[i][0] && check[i][1] && check[i][2])
      ans = true;
    else if(check[0][i] && check[1][i] && check[2][i])
      ans = true;
  }
  if(check[1][1] && check[2][2] && check[0][0] || check[0][2] && check[1][1] && check[2][0])
    ans = true;

  if(ans)
    cout << "Yes" << endl;
  else
    cout << "No"  << endl;
  return 0;
}
