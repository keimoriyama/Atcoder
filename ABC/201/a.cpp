#include <string>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


int main()
{
    vector<int> A(3, 0);
    for(int i = 0; i < 3; i++)
        cin >> A[i];
    sort(A.begin(), A.end());
    /*
    for(int i = 0; i < 3; i++)
        cout << A[i] << " ";
    cout << endl;
    */
    if(A[0] -  A[1] ==  A[1] - A[2])
        cout << "Yes" << endl;
    else
        cout << "No" << endl;
    return 0;
}
