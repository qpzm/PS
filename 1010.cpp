#include <iostream>

using namespace std;
int table[30][30] = {0};
int bridgeCount(int m, int n){
  int result = 0;
  int m_idx = m-1, n_idx = n-1;
  if(m == 1) return n;
  if(m == n) return 1;
  if(table[m_idx][n_idx] != 0) return table[m_idx][n_idx];
  for(int i=m-1; i<n; i++){
    result += bridgeCount(m-1, i);
  }
  table[m_idx][n_idx] = result;
  return result;
}

int main(){
  int T,m,n;
  cin >> T;
  for(int i=0; i<T; i++){
    cin >> m >> n; //문제의 정의와는 M,N  반대
    cout << bridgeCount(m, n) << endl;
  }
}
