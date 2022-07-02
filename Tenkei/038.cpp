#include <iostream>
#include <string>
#include <vector>
using namespace std;

long long gcd(long long x, long long y){
	if(y == 0)
		return x;
	else
		return gcd(y, x % y);
}

int main() {
	long long A, B, d, ans;
	long long t = 1000000000000000000LL;
	cin >> A >> B;
	d = gcd(A, B);
	ans = B / d;
	if(ans > t / A)
		cout << "Large" << endl;
	else
		cout << ans * A << endl;
	return 0;
}
