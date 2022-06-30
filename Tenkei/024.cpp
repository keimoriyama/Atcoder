#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main(int argc, char* argv[]) {
	long long N, K;
	cin >> N >> K;
	vector<long long> A(N), B(N);
	for(int i = 0; i < N; i++)
		cin >> A[i];
	for(int i = 0; i < N; i++)
		cin >> B[i];
	long long diff = 0;
	for(int i = 0; i < N; i++)
		diff = diff + abs(A[i] - B[i]);
	if(K < diff)
		cout << "No" << endl;
	else if((K - diff) % 2 == 0)
		cout << "Yes" << endl;
	else
		cout << "No" << endl;
	return 0;
}
