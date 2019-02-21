#include <iostream>

using namespace std;

int main(){
  int T,m,n,i;
  int ret; //30C15 = 155117520
  cin >> T;
  while(T--){
    cin >> n >> m; // by problem's def
    for(i=ret=1; i<=n; i++){
      ret *= (m+1-i);
      ret /= i;
    }
    cout << ret << endl;
  }
}
