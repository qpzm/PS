#include <cstdio>
#include <utility>
#define MAX_ROW (3<<10)
#define MAX_COL ((6<<10)-1)

using namespace std;
typedef pair<int, int> Point;
typedef pair<int, int> Size;
char arr[MAX_ROW][MAX_COL];
void sol(Size, Point);

int main() {
  int i,j,tmp,row_size, col_size=6;
  scanf("%d", &row_size);
  tmp = row_size;
  while(tmp != 3) {
    tmp = tmp >> 1;
    col_size = col_size << 1;
  }
  col_size--;

  sol(make_pair(row_size, col_size), make_pair(0,MAX_COL/2));

  for(i=0; i < row_size; i++) {
    for(j=MAX_COL/2 - col_size/2; j <= MAX_COL/2 + col_size/2; j++) {
      if(arr[i][j] == '\0') printf("%c", ' ');
      else printf("%c", arr[i][j]);
    }
    printf("\n");
  }
}

void sol(Size s, Point p){
  int x = p.first;
  int y = p.second;
  Size new_size = make_pair(s.first / 2, (s.second - 1) / 2);

  if(s.first == 3) {
    arr[x][y] = '*';
    arr[x+1][y-1] = '*';
    arr[x+1][y+1] = '*';
    for(int i=-2; i<=2; i++) arr[x+2][y+i] = '*';
    return;
  }

  int new_new_col_size = (new_size.second - 1) / 2;
  sol(new_size,make_pair(x,y));
  sol(new_size,make_pair(x+new_size.first, y-new_new_col_size-1));
  sol(new_size,make_pair(x+new_size.first, y+new_new_col_size+1));
}
