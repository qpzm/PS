#include <iostream>
#include <vector>
#include <map>

using namespace std;

vector<long long> solution(long long k, vector<long long> room_reqs) {
    vector<long long> results = {room_reqs[0]};
    map<long long, long long> intervals = {{room_reqs[0], room_reqs[0]}};
    for(auto it = ++room_reqs.begin(); it != room_reqs.end(); it++) {
        long long q = *it;
        auto search = intervals.lower_bound(q);

        if (search != intervals.end() && search->first == q) {
            search->second += 1;
            results.push_back(search->second);
        }
        else if(search != intervals.begin() && q <= prev(search)->second) {
            search = prev(search);
            search->second += 1;
            results.push_back(search->second);
        }
        else {
            intervals[q] = q;
            search = intervals.find(q);
            results.push_back(q);
        }

        auto next_search = next(search);
        if(next_search != intervals.end() &&
                search->second == next_search->first - 1) {
            search->second = next_search->second;
            intervals.erase(next_search);
        }

        auto prev_search = prev(search);
        if(search != intervals.begin() &&
                prev_search->second + 1 == search->first) {
            prev_search->second = search->second;
            intervals.erase(search);
        }
    }
    return results;
}

int main() {
    long long k = 10;
    vector<long long> room_reqs = {1,3,4,1,3,5};
    vector<long long> answer = solution(k, room_reqs);
    for(auto x: answer) {
        cout << x << ' ';
    }
    cout << '\n';
}
