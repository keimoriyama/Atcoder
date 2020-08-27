#include <iostream>
#include <string>
#include <vector>

using namespace std;
int N,M,before = -1;
bool is_tree = true;
vector<int> visited(100);

void dfs(vector<vector<int> >,int );


int main(int argc, char *argv[])
{
  cin >> N >> M;
  vector<int> u(N+1),v(N+1);
  vector<vector<int> > G(N+1 , vector<int>(N+1));
  int cnt = 0;
  for (int n = 0; n < M; n++) {
    cin >> u.at(n) >> v.at(n);
  }
  for (int n = 0; n < N+1; n++) {
    G.at(u.at(n)).at(v.at(n)) = 1;
    G.at(v.at(n)).at(u.at(n)) = 1;
    G.at(n).at(n) = 1;
    visited.at(n) = 0;
  }
  for(int i = 1;i < N+1; i++){
    for(int j = 1;j < N+1; j++){
      cout << G.at(i).at(j);
    }
    cout << endl;
  }
  for(int i = 1; i < N+1 ; i++){
    if(visited.at(i) == 0){
      dfs(G,i);
      if(is_tree){
        cnt++;
        cout << i << endl;
      }
      else
        is_tree = true;
    }
  }
  cout << cnt << endl;
  return 0;
}

void dfs(vector<vector<int> > g, int i){
  if(i == before)
    return;
  if(visited.at(i) == 1){
    cout << i << " "  << before << endl;
    is_tree = false;
    return;
  }
  visited.at(i) = 1;
  before = i;
  for (int n = 0; n < N; n++) {
    if(g.at(i).at(n) == 1 && visited.at(i) == 0)
      dfs(g,n);
  }
  visited.at(i) = 2;
}
