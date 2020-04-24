#include <unordered_map>
#include <iostream>
#include <algorithm>

using namespace std;

//int my_lower_bound(vector<int> v, int num) {
    //int interval = v.size() / 2;
    //int i = 0;
    //while(interval) {
        //while(i + interval < v.size() && v[i + interval] < num)
            //i = i + interval;
        //interval /= 2;
    //}
    //return i;
//}

//int my_upper_bound(vector<int> v, int num) {
    //int interval = v.size() / 2;
    //int i = 0;
    //while(interval) {
        //while(i + interval < v.size() && v[i + interval] <= num)
            //i = i + interval;
        //interval /= 2;
    //}
    //return i;
/*}*/

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    int N, M;
    unordered_map<int, int> map;
    cin >> N;
    while(N--) {
        int key;
        cin >> key;
        auto it = map.find(key);
        if(it != map.end())
            it->second += 1;
        else
            map.insert({key, 1});
    }
    cin >> M;
    while(M--) {
        int key;
        cin >> key;
        auto it = map.find(key);
        if(it != map.end())
            cout << it->second << ' ';
        else
            cout << 0 << ' ';
    }
    return 0;
}
