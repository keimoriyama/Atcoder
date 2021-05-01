#include <string>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N;

int next_combination(int sub){
    int x = sub & -sub, y = sub+x;
    return(((sub & ~y)/x) >> 1) | y;
}

int main()
{
    cin >> N;
    int64_t A[N],B[N],C[N],D[N],E[N];
    int64_t a[3],b[3],c[3],d[3],e[3];
    int64_t a_max,b_max,c_max,d_max,e_max;
    for(int i = 0; i < N; i++){
        cin >> A[i] >> B[i] >> C[i] >> D[i] >> E[i];
    }
    int k = 3;
    for(int bit = (1<<k) - 1; bit < (1 << N);bit = next_combination(bit)){
        vector<int> S;
        for(int i = 0; i < N; i++){
            if(bit & (1 << i))
                S.push_back(i);
        }
        for(int i = 0; i < S.size(); i++){
            a[i] = A[S[i]];
            b[i] = B[S[i]];
            c[i] = C[S[i]];
            d[i] = D[S[i]];
            e[i] = E[S[i]];
            a_max = *max_element(a, a+3);
            b_max = *max_element(b, b+3);
            c_max = *max_element(c, c+3);
            d_max = *max_element(d, d+3);
            e_max = *max_element(e, e+3);

        }
    }
    return 0;
}
