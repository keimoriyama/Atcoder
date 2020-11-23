#include <iostream>
#include <string>
#include <vector>

using namespace std;
int N;

void print_array(vector<int> A){
  for(int i = 0; i < N; i++)
    cout << A.at(i) << " ";
  cout << endl;
}

int main(int argc, char *argv[])
{
  int max = 0, tmp, GCD = 0;
  int ans = 0, GDC_max = 0;
  cin >> N;
  vector<int > A(N);
  for(int i = 0; i < N; i++){
    cin >> tmp;
    if(tmp > max)
      max = tmp;
    A.at(i) = tmp;
  }
  for(int i = 2; i <= max; i++){
    for(int j = 0; j < N;j++){
      if((A.at(j) % i) == 0)
        GCD++;
    }
    //cout << "i:" << i << " GCD:" << GCD << endl;
    if(GDC_max < GCD){
      GDC_max = GCD;
      ans = i;
    }
    GCD = 0;
  }
  cout << ans << endl;

  return 0;
}
