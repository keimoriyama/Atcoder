#include <string>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


int main()
{
    int n;
    long long k;
    long long x, y;
    vector<pair<long long, long long> > a;
    cin >> n >> k;
    for(int i = 0;i < n; i++){
        cin >> x >> y;
        a.push_back(make_pair(x,y));
    }
    sort(a.begin(), a.end());
    for(int i = 0; i < n; i++){
        if(a[i].first>k)break;
        k += a[i].second;
    }
    cout << k << endl;
    return 0;
}
