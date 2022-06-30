#include <iostream>
#include <string>
#include <vector>
using namespace std;

long long gcd(long long x, long long y){
	if (y != 0){
		return gcd(y, x % y);
	}
	return x;
}


long long A, B, C;
int main(int argc, char* argv[]) {
	cin >> A >> B >> C;
	long long a = gcd(A, B);
	long long com_gcd = gcd(a, C);
	long long ans = (A / com_gcd - 1LL) + (B / com_gcd - 1LL) + (C / com_gcd - 1LL);
	cout << ans << endl;
	return 0;
}
