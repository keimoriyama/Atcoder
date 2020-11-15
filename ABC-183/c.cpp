#include <iostream>
#include <string>
#include <vector>

using namespace std;
int ans = 0, score = 0;

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


int main(int argc, char *argv[])
{
  int N,K;
  cin >> N >> K;
  vector<vector< int> > G(N, vector<int>(N));
  vector<bool> visit(N);
  for(int i = 0; i < N; i++){
    for(int j = 0; j < N; j++){
      cin >> G.at(i).at(j);
    }
  }
  dfs(0,N,G,visit,K);
  cout << ans << endl;
  return 0;
}
