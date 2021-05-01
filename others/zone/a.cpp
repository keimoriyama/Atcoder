#include <string>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

string input;

vector<int> find_all(string str, string substr){
    vector<int> result;

    int substrSize = substr.size();
    int pos = str.find(substr);

    while(pos != string::npos){
        result.push_back(pos);
        pos = str.find(substr, pos + substrSize);
    }
    return result;
}

int main()
{
    string str = "ZONe";
    cin >> input;

    vector<int> result = find_all(input, str);

    cout << result.size() << endl;

    return 0;
}
