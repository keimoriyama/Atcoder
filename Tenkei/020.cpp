#include <iostream>
#include <string>
#include <vector>
#include <cmath>
using namespace std;

long double a, b, c;
int main(int argc, char* argv[]) {
	cin >> a >> b >> c;
	long double log_a = a;
	long double log_bc = powl(c, b);
	if (log_a < log_bc){
		cout << "Yes" << endl;
	}else{
		cout << "No" << endl;
	}
	return 0;
}
