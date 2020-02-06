#include <iostream>
using namespace std;
int main(){
  int T,a,b;
  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
  cin >> T;
  while(T--){
    cin >> a >> b;
    cout << a + b << '\n';
  }
}
