#include <iostream>
#include <string>
#include <vector>

using namespace std;


int main()
{
   	long A, B, C;
    long a, b, c;
    cin >> a >> b >> c;
    A = a*a;
    B = b*b;
    C = c*c;
    if(A+B<C)cout << "Yes" << endl;
    else cout << "No" << endl;
    return 0;
}
