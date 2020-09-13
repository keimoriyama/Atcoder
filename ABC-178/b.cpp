#include <iostream>
#include <vector>

using namespace std;

int main()
{
    long long a, b, c, d, max;
    vector<long long> ans(4);
    cin >> a >> b >> c >> d;
    /*
    for (i = a; i <= b; i++)
    {
        for (j = c; j <= d; j++)
        {
            tmp = i * j;
            if (tmp >= max)
            {
                max = tmp;
            }
        }
    }
    */
    ans[0] = a * c;
    ans[1] = a * d;
    ans[2] = b * c;
    ans[3] = b * d;
    max = ans[0];
    for (int i = 0; i < 4; i++)
    {
        if (ans[i] >= max)
            max = ans[i];
    }
    cout << max << endl;
}