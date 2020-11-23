#include <iostream>
#include <string>

using namespace std;

void dfs(int i, int j);

int H,W;
char maze[500][500];
int visited[500][500];

int main(int argc, char *argv[])
{
  int start_i,start_j;
  int goal_i,goal_j;
  cin >> H >> W;
  for (int i = 0; i < H; i++) {
    for (int j = 0; j < W; j++) {
      cin >> maze[i][j];
      visited[i][j] = 0;
      if(maze[i][j] == 's'){
        start_i = i;
        start_j = j;
      }
      if(maze[i][j] == 'g'){
        goal_i = i;
        goal_j = j;
      }
    }
  }
  dfs(start_i,start_j);
  if(visited[goal_i][goal_j] == 1)
    cout << "Yes" << endl;
  else
    cout << "No" << endl;
  return 0;
}

void dfs(int i, int j){
  if(i >= H || j >= W || i < 0 || j < 0 || maze[i][j] == '#')
    return;
  if(visited[i][j] == 1)
    return;
  visited[i][j] = 1;
  dfs(i+1,j);
  dfs(i,j+1);
  dfs(i-1,j);
  dfs(i,j-1);
}
