#include <iostream>
#include <string>
#include <queue>
#include <vector>

using namespace std;


int main(int argc, char *argv[])
{
  char tmp;
  queue<int> queue_x,queue_y;
  int R,C,sy,sx,gy,gx;
  bool flag = false;
  int dx[4] = {1,0,-1,0};
  int dy[4] = {0,1,0,-1};
  vector<vector<int> > visited;
  cin >> R >> C;
  cin >> sy >> sx;
  cin >> gy >> gx;
  sx--;sy--;gx--;gy--;
  vector<vector<int> > c(R , vector<int>(C));
  for (int i = 0; i < R; i++) {
    for (int j = 0; j < C; j++) {
      cin >> tmp;
      if(tmp == '#')
        c.at(i).at(j) = 0;
      else
        c.at(i).at(j) = 1;
    }
  }
  visited.assign(R,vector<int>(C,0));
  queue_x.push(sx);
  queue_y.push(sy);
  while(queue_x.empty() && queue_y.empty()){
    int x,y;
    x = queue_x.front();
    y = queue_y.front();
    queue_x.pop(); queue_y.pop();
  for (int i = 0; i < R; i++) {
    for (int j = 0; j < C; j++) {
      cout << visited.at(i).at(j) << "  ";
    }
    cout << endl;
  }
  if(flag)
    cout << "done" << endl;
  else
    cout << "false" << endl;
  return 0;
}
