#include <vector>
#include <string.h>
#include <iostream>
using namespace std;
#define rep(i,n) for(int i=0; i<(n); ++i)
using Graph = vector<vector<int> >;
 
vector<bool> seen;
bool dfs(const Graph &G, int v, int p=-1){
    bool ret = true;
    seen[v] = true;
    for(auto nv: G[v]){
        //nvがvの親pであるならcontinue
        if(nv==p) continue;
        //その他でもし走査済の頂点に行ったなら木ではないので更新
        if(seen[nv]){
            ret = false;
            continue;
        }
        //走査していない点の情報を追加
        //もしそこでサイクルがあったなら無理
        ret &= dfs(G, nv, v);
    }
    return ret;
}
 
int main(){
    int n,m; cin >> n >> m;
    Graph G(n);
 
    rep(i,m){
        int a,b; cin >> a >> b;
        a--,b--;
        G[a].push_back(b);
        G[b].push_back(a);
    }
 
    int count = 0;
    seen.assign(n, false);
    rep(v,n){
        if(seen[v]) continue;
        //グラフを走査した結果木であったならカウント
        if(dfs(G, v)) ++count;
    }
 
    cout << count << endl;
}
