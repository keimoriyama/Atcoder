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
  //for (int i = 0; i < R; i++) {
  //  for (int j = 0; j < C; j++) {
  //    cout << c.at(i).at(j) ;
  //  }
  //  cout << endl;
  //}
  visited.assign(R,vector<int>(C,0));
  queue_x.push(sx);
  queue_y.push(sy);
  visited.at(sx).at(sy) = 1;
  while(!queue_x.empty() && !queue_y.empty()){
    int x,y;
    x = queue_x.front();
    y = queue_y.front();
    //cout << "x: " << x << " y: " << y <<endl;
    //cout << "visited: " << visited.at(x).at(y) << endl;
    queue_x.pop(); queue_y.pop();
    for(int i = 0; i < 4; i++){
      //迷路の中の点のときにキューに入れる
      if(x+dx[i] >= 0 && x+dx[i] < R && y+dy[i] >= 0 && y+dy[i] < C &&
          c.at(x+dx[i]).at(y+dy[i]) == 1 && visited.at(x+dx[i]).at(y+dy[i]) == 0){
        queue_x.push(x+dx[i]);
        queue_y.push(y+dy[i]);
        visited.at(x+dx[i]).at(y+dy[i]) = visited.at(x).at(y) + 1;
      }
    }
  }
  cout << visited.at(gy).at(gx) -1 << endl;
  return 0;
}
