#include <iostream>
#include <string>
#include <vector>

using namespace std;

int N, ans = 0;

void print_array(vector<vector<int> > v){
  for(int i = 0;i < N;i++){
    cout << v.at(i).at(0) << " " << v.at(i).at(1) << endl;
  }
}

int main(int argc, char *argv[])
{
  bool flag = false;
  cin >> N;
  vector<vector<int> > D(N, vector<int>(N));
  for(int i = 0; i < N; i++){
    cin >> D.at(i).at(0) >> D.at(i).at(1);
  }
  //print_array(D);
  for(int i = 0;i < N;i++){
    //cout << D.at(i).at(0) << " " << D.at(i).at(1) << endl;
    //cout << ans << endl;
    if(D.at(i).at(0) == D.at(i).at(1)){
      ans+=1;
    }
    else{
      ans = 0;
    }
    if(ans == 3){
      flag  = true;
    }
  }
  if(flag){
    cout << "Yes" << endl;
  }
  else{
    cout << "No" << endl;
  }
  return 0;
}
