#include <string>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


int main()
{
    int N;
    cin >> N;
    vector<pair<int ,string> > M(N);
    for(int i = 0; i < N; i++){
        cin >> M[i].second >> M[i].first;
    }
    sort(M.begin(), M.end());
    /*
    for(int i = 0; i < N; i++){
        cout << M[i].first<< " " << M[i].second << endl;
    }
    */
    cout << M[N-2].second << endl;
    return 0;
}
