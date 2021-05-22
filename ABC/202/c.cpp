#include <string>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool bi_search(vector<int> &a, int target){
    int right, left, mid;
    right = a.size()-1;
    left = 0;
    while(right >= left){
        mid = (right+left)/2;
        //cout << mid << " " << a[mid] << " " << target << endl;
        if(a[mid] == target)return true;
        else{
            if(a[mid] > target)right= mid-1;
            else left = mid+1;
        }
    }
    return false;
}

int main()
{
    int N;
    long long ans = 0;
    cin >> N;
    vector<int> bin(N, 0);
    vector<int> a(N), b(N), c(N);
    for(int j = 0; j < N; j++){
        cin >> a[j];
        bin[a[j]]++;
    }
    for(int j = 0; j < N; j++)
        cin >> b[j];
    for(int j = 0; j < N; j++)
        cin >> c[j];
    stable_sort(a.begin(), a.end());
    for(int i = 0; i < N; i++){
        if(bi_search(a, b[c[i] - 1])){
            ans = ans + bin[b[c[i] - 1]];
        }
    }
    cout << ans << endl;
    return 0;
}
