#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int n;
    long long ans = 0;
    cin >> n;
    int i, j;
    /*
    for (i = 0; i < n; i++)
    {
        for (j = i + 1; j < n; j++)
        {
            ans++;
        }
    }
    */
    long long a10 = 10, a8 = 8;
    for (long long i = 0; i < n; i++)
    {
        a10 *= 10;
        a8 *= 8;
    }
    ans = a10 - a8;
    cout << ans << endl;
}