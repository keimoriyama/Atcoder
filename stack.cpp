#include <stack>
#include <cstdio>

using namespace std;

int main(){
  stack<int> s;
  s.push(1);
  s.push(2);
  s.push(3);
  printf("%d\n",s.top());
  s.pop();
  s.push(4);
  printf("%d\n",s.top());
  return 0;
}

