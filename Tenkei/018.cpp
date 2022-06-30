#include <iostream>
#include <string>
#include <vector>
#include <cmath>
using namespace std;
long double PI = 3.14159265358979;

int main(int argc, char* argv[]) {
	long double T, L, X, Y, Q, e;
	long double theta, y, z, dist1, dist2;
	cin >> T >> L >> X >> Y >> Q;
	for(int i = 0; i < Q; i++){
		cin >> e;
		long double y = -(L / 2.0) * sin(e / T * 2.0 * PI);
		long double z = (L / 2.0) * (1.0 - cos(e / T * 2.0 * PI));
		long double d1 = sqrt(X * X + (y - Y) * (y - Y));
		long double d2 = z;
		long double theta = atan2(d2, d1);
		printf("%.12Lf\n", theta * 180.0L / PI);
	}
	return 0;
}
