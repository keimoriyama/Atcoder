#include <string>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int N,D,H;

int main(){
    cin >> N >> D >> H;
    double d[N], h[N];
    double ang[N];
    double max = 0;
    for(int i = 0; i < N; i++){
        cin >> d[i] >> h[i];
    }
    for(int i = 0; i < N; i++){
        ang[i] = atan((H-h[i])/(D-d[i]));
    }
    for(int i = 0; i < N; i++){
        //cout << ang[i] << " " << endl;
        //cout << H - D*tan(ang[i]) << " " << endl;
        if(H-D*tan(ang[i]) > max){
            max = H-D*tan(ang[i]);
        }
    }
    cout << max << endl;
    return 0;
}
