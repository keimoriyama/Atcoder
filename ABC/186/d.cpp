#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int N, ans = 0;
    cin >> N;
    vector<int> A(N + 1);
    for (int i = 1; i <= N; i++)
    {
        cin >> A[i];
    }
    for (int i = 1; i <= (N - 1); i++)
    {
        for (int j = i + 1; j <= N; j++)
        {
            //cout << "A[i] " << A[i] << " A[j] " << A[j] << endl;
            ans = ans + abs(A[i] - A[j]);
        }
    }
    cout << ans << endl;
    return 0;
}