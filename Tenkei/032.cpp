#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;

int N, M;
vector<vector<int>> A(12, vector<int>(12, 0));
vector<vector<bool>> kenaku(12, vector<bool>(12, false));
vector<int> X, Y;

int main(int argc, char* argv[]) {	
	cin >> N;
	for(int i = 1; i <= N; i++){
		for(int j = 1; j <= N; j++)
			cin >> A[i][j];
	}
	cin >> M;
	int x, y;
	for(int i = 0; i < M; i++){
		cin >> x >> y;
		kenaku[x][y] = true;
		kenaku[y][x] = true;
	}

	vector<int> p;
	for(int i = 1; i <= N; i++)p.push_back(i);

	int ans = (1 << 30);	
	do{
		bool flag = true;
		int sum = 0;
		for(int i = 0; i < N - 1; i++){
			if(kenaku[p[i]][p[i + 1]] == true) flag = false;
		}
		for(int i = 0; i < N; i++){
			sum += A[p[i]][i + 1];
		}
		if(flag == true)ans = min(ans, sum);
	}while(next_permutation(p.begin(), p.end()));

	if(ans == (1 << 30))
		ans = -1;
	cout << ans << endl;
	return 0;
}
