#include <iostream>
#include <string>
#include <vector>

#define MAX_N 1001

using namespace std;
int N;

void print_array(int *a){
	for(int i = 0; i < MAX_N;i++)
        cout << a[i] << " ";
    cout << endl;
}

int main()
{
    cin >> N;
    int A[N], B[N], num[MAX_N];
    int x, y;
    int ans = 0;
    for(int i = 0; i< N;i++)cin >> A[i];
    for(int i = 0; i< N;i++)cin >> B[i];
    for(int i = 0; i<MAX_N;i++)num[i] = 1;
    //cout << "num ";
    //print_array(num);
    for(int i = 0; i<N; i++){
		x = A[i];
        y = B[i];
        for(int j = 1; j < x; j++)num[j] = 0;
        for(int j =MAX_N; j > y; j--)num[j] = 0;
        //cout << "num ";
        //print_array(num);
    }
    for(int i = 1; i < MAX_N; i++){
        if(num[i] == 1)ans++;
    }
    cout << ans << endl;
    return 0;
}
