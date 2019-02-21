#include <iostream>
#include <string>
using namespace std;
int main(){
    int n;
    string str;
    cin >> n;
    for(int i=1; i<=n; ++i){
        str = "";
        for(int j=1; j<=i; ++j){
            str+= "*";
        }
        cout << str << endl;
    }
    return 0;
}
