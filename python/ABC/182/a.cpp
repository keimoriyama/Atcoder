#include <iostream>
#include <string>
#include <vector>

using namespace std;


int main(int argc, char *argv[])
{
  int A, B, follow;
  cin >> A >> B;
  follow= 2*A+100;
  cout << follow - B << endl;
  return 0;
}
