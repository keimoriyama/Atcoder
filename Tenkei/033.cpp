#include <iostream>
#include <string>
#include <vector>
using namespace std;

int H, W;

int main(int argc, char* argv[]) {
	cin >> H >> W;	
	if(H == 1 || W == 1)cout << H * W << endl;
	else cout << ((H + 1) / 2) * ((W + 1) / 2 ) << endl;
	return 0;
}
