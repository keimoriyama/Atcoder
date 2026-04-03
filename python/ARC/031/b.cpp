#include <iostream>
#include <string>

using namespace std;

int map[10][10];
int visited[10][10];
int dx[4] = {1,0,-1,0};
int dy[4] = {0,1,0,-1};

void dfs(int , int);
int check();
void reset_flag();

int main(int argc, char *argv[])
{
  char tmp;
  bool flag = false;
  int start_i,start_j;
  for (int i = 0; i < 10; i++) {
    for (int j = 0; j < 10; j++) {
      cin >> tmp;
      if(tmp == 'x')
        map[i][j] = 0;
      if(tmp == 'o'){
        if(!flag){
          start_i = i;
          start_j = j;
          flag = true;
        }
        map[i][j] = 1;
      }
      visited[i][j] = 0;
    }
  }
  int res = 0;
  for (int i = 0; i < 10; i++) {
    for (int j = 0; j < 10; j++) {
      if(map[i][j] == 0){
        map[i][j] = 1;
        dfs(start_i,start_j);
        res = check();
        if(res == 1)
          break;
        map[i][j] = 0;
        reset_flag();
      }
      if(res == 1)
        break;
    }
    if(res == 1)
      break;
  }
  if(res == 1)
    cout << "YES" << endl;
  else
    cout << "NO" << endl;
  return 0;
}

void dfs(int i,int j){
  if(i >= 10 | j >= 10 | i < 0 | j < 0 | map[i][j] == 0){
    return;
  }
  if(visited[i][j]){
    return;
  }
  visited[i][j] = 1;
  for(int k = 0; k < 4; k++)
    dfs(i+dx[k],j+dy[k]);
}

int check(){
  for (int n = 0; n < 10; n++) {
    for (int m = 0; m < 10; m++) {
      if(map[n][m] != visited[n][m])
        return 0;
    }
  }
  return 1;
}

void reset_flag(){
  for(int i = 0; i < 10; i++){
    for(int j = 0; j < 10; j++){
      visited[i][j] = 0;
    }
  }
}
