#include <iostream>
#include <cstring>

using namespace std;
int max(int x, int y){
  return x>=y ? x : y;
}

int LCS(char x[],char y[], int m, int n){
  int c[m+1][n+1];
  for(int i=0; i<m+1; i++){
    for(int j=0; j<n+1; j++){
      if(i == 0 || j == 0) c[i][j] = 0;
      else if (x[i-1] == y[j-1]) c[i][j] = 1 + c[i-1][j-1];
      else c[i][j] = max(c[i-1][j], c[i][j-1]);
    }
  }
  return c[m][n];
}

int main(){
  char x[1001], y[1001];
  int m,n;
  cin >> x;
  cin >> y;

  m = strlen(x); n = strlen(y);

  printf("%d\n", LCS(x,y ,m,n));
  return 0;
}
