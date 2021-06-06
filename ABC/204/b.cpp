#include <string>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int N;
    int ans = 0;
    cin >> N;
    vector<int> A(N,0);
    for(int i = 0; i < N; i++)
        cin >> A[i];
    for(int i = 0; i < N; i++){
        if(A[i] > 10)
            ans += A[i]-10;
    }
    cout << ans << endl;
    return 0;
}
