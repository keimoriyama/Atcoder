#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int H, W;
    int min_element = 1000, ans = 0;
    cin >> H >> W;
    vector<vector<int>> A(H, vector<int>(W, 0));
    for (int i = 0; i < H; i++)
    {
        for (int j = 0; j < W; j++)
        {
            cin >> A[i][j];
            if (A[i][j] < min_element)
                min_element = A[i][j];
        }
    }

    for (int i = 0; i < H; i++)
    {
        for (int j = 0; j < W; j++)
        {
            ans += A[i][j] - min_element;
        }
    }
    cout << ans << endl;
}