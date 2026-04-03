#include <iostream>
#include <string>
using namespace std;

int
main(int argc, char* argv[]) {
  int N;
  cin >> N;
  int L[N];
  int i,j,k,ans;
  int len1,len2,len3;
  ans = 0;
  for(i = 0; i < N; i++){
    cin >> L[i];
  }
  for(i = 0; i < N; i++){
    for(j = i+1; j < N; j++){
      for(k = j+1; k < N; k++){
        len1 = L[i];
        len2 = L[j];
        len3 = L[k];
        if(len1 != len2 && len2 != len3 && len3 != len1){
          if((len3+len2)>len1 && (len1+len2)>len3 && (len3+len1)>len2){
            ans++;
        }
        }
     }
    }
  }
  cout << ans << endl;
  return 0;
}
