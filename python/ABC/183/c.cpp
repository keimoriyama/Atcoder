#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;
int ans = 0, score = 0;
/*
bool checkflag(vector<bool> visit, int N){
  for(int i = 0; i < N ; i++){
    if(visit.at(i) != 1)
      return false;
  }
  return true;
}

void dfs(int i, int N,vector<vector< int> > G, vector<bool> visit, int K ){
  if(checkflag(visit, N) && score == K){
    ans++;
  }
  if(i < 0 | i > N){
    return;
  }
  visit.at(i) = true;
  for(int j = 0; j < N; j++){
    if(i != j && visit.at(j) == false){
      score = score+ G.at(i).at(j);
      dfs(j, N, G, visit,K);
      score = score- G.at(i).at(j);
    }
  }
  visit.at(i) = false;
}

*/
int main(int argc, char *argv[])
{
  int N, K;
  cin >> N >> K;
  vector<vector<int>> G(N, vector<int>(N));
  vector<int> visit(N);
  for (int i = 0; i < N; i++)
  {
    for (int j = 0; j < N; j++)
    {
      cin >> G.at(i).at(j);
    }
  }
  for (int i = 0; i < N; i++)
    visit.at(i) = i;
  do
  {
    score = 0;
    for (int i = 0; i < N; i++)
      // 都市1に戻ってくることを考えている（i+1)%Nの部分
      score += G.at(visit[i]).at(visit[(i + 1) % N]);
    if (score == K)
      ans++;
    //順列の生成
  } while (next_permutation(visit.begin() + 1, visit.end()));
  cout
      << ans << endl;
  return 0;
}
