#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;

int main(int argc, char* argv[]) {
	long long N;
	string s;
	cin >> N;
	map<string, int> Map;
	vector<string> S(N);
	for(int i = 0; i < N; i++)
		cin >> S[i];
	for(int i = 0; i < N; i++){
		if(Map[S[i]] == 0)cout << i+1 << endl;
		Map[S[i]] = 1;
	}
	return 0;
}
