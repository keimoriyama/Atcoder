#include <iostream>
#include <string>
#include <vector>

using namespace std;


int main()
{
    int N, Q;
    int T,A,B;
    std::string S, tmp;
    cin >> N >> S >> Q;
    for(int i = 0; i < Q; i++){
        cin >> T >> A >> B;
        A--;
        B--;
        if(T == 1){
            //swap S[A] & S[B]
            tmp = S[B];
            S.replace(B, 1, 1, S[A]);
            S.replace(A, 1, tmp);
        }
        if(T == 2){
            // swap S[:N] & S[N:]
            tmp = S.substr(0, N);
        	S.replace(0,N,S.substr(N, 2*N));    
        	S.replace(N,2*N,tmp);    
        }
    }
    cout << S << endl;
    return 0;
}
