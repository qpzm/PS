#include <cstdio>
#include <utility>

using namespace std;
typedef pair<int, int> point;
char arr[6561][6561];
void sol(int size, point p);

int main() {
  int i,j,size;
  scanf("%d", &size);
  sol(size, make_pair(0,0));

  for(i=0;i<size;i++) {
    for(j=0;j<size;j++) {
      if(arr[i][j] == '\0') {
        printf("%c", ' ');
      }
      else printf("%c", arr[i][j]);
    }
    printf("\n");
  }
}

void sol(int size, point p){
  int x = p.first;
  int y = p.second;
  int new_size = size / 3;

  if(size == 1) {
    arr[x][y] = '*';
    return;
  }

  for(int i=0; i<3; i++){
    for(int j=0; j<3; j++){
      if(!(i == 1 && j == 1)) {
        sol(new_size, make_pair(x + i * new_size, y + j * new_size));
      }
    }
  }
}
