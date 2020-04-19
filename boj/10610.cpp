#include <iostream>
#include <algorithm>
#include <string>
#include <cstdlib>
using namespace std;
bool comp (int i,int j) { return (i>j); }
int main() {
    string num;
    char c_arr[1];
    int sum = 0;
    getline(cin, num);
    for(auto c : num) {
        c_arr[0] = c;
        sum += atoi(c_arr);
    }
    if(sum % 3 != 0)
        cout << -1 << '\n';
    else {
        sort(num.begin(), num.end(), comp);
        if(num.back() != '0')
            cout << -1 << '\n';
        else
            cout << num;
    }
    return 0;
}
