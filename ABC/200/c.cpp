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
    int ans = 0;
    for(int i = 0; i < N; i++)
        cin >> a[i];
    //sort(a, a+N);
    for(int i = 0; i < N; i++){
        for(int j = i+1; j < N; j++){
            /*
            if(a[i]%100 != a[j]%100)continue;
            if(((a[i]/100)-(a[j]/100))%2 != 0)continue;
            */
            if((a[i]-a[j])%200 != 0)continue;
            //cout << "i: " << i << " j: " << j << endl;
            ans++;
        }
    }
    cout << ans << endl;
    return 0;
}
