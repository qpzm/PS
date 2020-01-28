#include <iostream>
#include <algorithm>
#include <string>

using namespace std;
int max(int x, int y){
  return x>=y ? x : y;
}

void LCS(string x,string y,int m, int n){
  int c[m+1][n+1];
  int b[m][n];
  for(int i=0; i<m+1; i++){
    for(int j=0; j<n+1; j++){
      if(i == 0 || j == 0) c[i][j] = 0;
      else if (x[i-1] == y[j-1]) {
        c[i][j] = 1 + c[i-1][j-1];
        b[i-1][j-1] = 3;
      }
      else {
        int up = c[i-1][j];
        int left = c[i][j-1];
        c[i][j] = max(up, left);
        if(up >= left) b[i-1][j-1] = 1;
        else b[i-1][j-1] = 2;
      }
    }
  }
 int i=m-1; int j=n-1;
 string rev_ret = "";
 string ret;
  while(i >= 0 && j >= 0){
    switch(b[i][j]){
      case 1: i--;break;
      case 2: j--; break;
      case 3: rev_ret.push_back(x[i]); i--; j--; break;
      default: cout << "error" << endl;
    }
  }
  ret = string(rev_ret);
  reverse(ret.begin(), ret.end());
  printf("%d\n", (int)ret.length());
  cout << ret << endl;
}

int main(){
  string x, y;
  int m,n;
  cin >> x;
  cin >> y;

  m = x.length(); n = y.length();
  LCS(x,y,m,n);
  return 0;
}
