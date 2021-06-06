#include <string>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<vector<int> > G;
vector<bool> flag(2000);

int N, M;

void dfs(int s) {
    //cout << "s: " << s << " depth: " << depth << endl;
    if (flag[s])
        return;
    flag[s] = true;
    for(auto vv:G[s])dfs(vv);
}

int main()
{
    cin >> N >> M;
    int a, b;
    long long ans = 0;
    G.resize(N);
    for (int i = 0; i < M; i++) {
        cin >> a >> b;
        G[a-1].push_back(b-1);
    }

    for (int i = 0; i < N; i++) {
        flag.assign(2000, false);
        dfs(i);
        for(int j =0; j < N; j++)
            if(flag[j])ans++;
    }
    cout << ans << endl;
    return 0;
}
