#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int main() {
  int N, D, result;
  double dis;
  result = 0;
  cin >> N >> D;
  vector<vector<int> > vec(N, vector<int>(2));
  for(int i = 0; i < N; i++){
    for(int j = 0; j < 2; j++){
      cin >> vec.at(i).at(j);
    }
  }
  for(int i = 0; i < N; i++){
    dis = sqrt(std::pow(vec.at(i).at(0),2) + std::pow(vec.at(i).at(1),2));
    if(dis <= D){
      result = result + 1;
    }
  }
  cout << result << endl;
  return 0;
}
