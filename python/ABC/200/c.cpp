#include <string>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


int main()
{
    int N;
    cin >> N;
    int a[N]; 
    long long b[200] = {0};
    long long ans = 0;
    for(int i = 0; i < N; i++){
        cin >> a[i];
        b[a[i]%200]++;
    }
    //sort(a, a+N);
    for(int i = 0; i < 200; i++){
            ans += (b[i]*(b[i]-1))/2;
    }
    cout << ans << endl;
    return 0;
}
