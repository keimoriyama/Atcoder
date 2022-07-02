#include <iostream>
#include <string>
#include <vector>
using namespace std;

long long N, Q;
long long T, x, y, t, i;

int main(int argc, char* argv[]) {
	cin >> N >> Q;
	vector<long long> A(N, 0);
	vector<int> index;
	for(i = 0; i < N; i++){
		cin >> A[i];
	}
	int shifts = 0;
	for(i = 0; i < Q; i++){
		cin >> T >> x >> y;
		x--;y--;
		if(T == 1){
			swap(A[(x + shifts) % N], A[(y + shifts) % N]);
		} else if(T == 2){
			shifts = (shifts + N - 1) % N;
		} else{
			cout << A[(x + shifts) % N] << endl;
		}
	}
	return 0;
}
