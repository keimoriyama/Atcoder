#include <string>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int x,y;
    vector<int> a(3,0);
    cin >> x >> y;
    a[x] = 1;
    a[y] = 1;
    if(x == y)cout << x << endl;
    else{
        for(int i =0; i < 3; i++){
            if(a[i] == 0)cout << i << endl;
        }
    }
    return 0;
}
