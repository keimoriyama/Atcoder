#include <iostream>
#include <string>
#include <vector>


using namespace std;

vector<bool> seen;
bool dfs(const vector<vector<int> > &G, int v, int p = -1){
  bool ret = true;
  seen[v] = true;
  for(auto nv: G[v]){
    if(nv == p)continue;
    if(seen[nv]){
      ret = false;
      continue;
    }
    ret &= dfs(G, nv, v);
  }
  return ret;
}

int main(int argc, char *argv[])
{
  int n,m; cin >> n >> m;
  vector<vector<int> > G(n);

  for (int n = 0; n < m; n++) {
    int a,b;
    cin >> a >> b;
    a--;b--;
    G[a].push_back(b);
    G[b].push_back(a);
  }
  int count = 0;
  seen.assign(n, false);
  for(int v = 1; v < n; v++){
    if(seen[v])continue;
    if(dfs(G, v))++count;
  }
  cout << count << endl;
  return 0;
}
