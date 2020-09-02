#include <iostream>
#include <string>
#include <vector>
#include <utility>
#include <algorithm>

using namespace std;

void print_vec(vector<int> vec,int N){
  for(int i = 0;i < N; i++){
    cout << vec.at(i) << " ";
  }
  cout << endl;
}


int main(int argc, char *argv[])
{
  int N,j,ans,len;
  j = 0;
  ans = 0,len = -1e9;
  cin >> N;
  vector<int> x(N),l(N);
  vector<pair<int ,int> > v(N);
  for(int i = 0; i < N;i++){
    cin >> x.at(i) >> l.at(i);
    v[i].first = x.at(i) - l.at(i);
    v[i].second = x.at(i) + l.at(i);
  }
  sort(v.begin(),v.end());
  for(int i = 0; i < N; i++){
    if(len <= v[i].first){
      ans++;
      len = v[i].second;
    }
  }
  cout << ans << endl;
  return 0;
}
