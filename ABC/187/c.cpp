#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main(){
    int N;
    bool flag = false;
    cin >> N;
    vector<string> S(N);
    string target;
    for(int i = 0; i < N; i++){
        cin >> S[i];
    }
    for(int i = 0; i < N; i++){
        target = S[i];
        if(target.find("!") == 0)
            target.erase(target.begin());
        else
            target = "!" + target;
        //cout << target << endl;
        for(int j = i+1; j < N; j++){
            if((S[j] == target) && !flag){
                if(target.find("!") == 0)
                    target.erase(target.begin());
                cout << target << endl;
                flag = true;
            }
        }
    }
    if(!flag){
        cout << "satisfiable" << endl;
    }
    return 0;
}