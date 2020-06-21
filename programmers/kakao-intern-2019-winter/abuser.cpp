#include <string>
#include <set>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

#define DEBUG(x) cerr << #x << " = " << x << endl;
#define DEBUGALL(x) { cerr << #x << " = "; for(const auto &e: x) cerr << e << " "; cerr << endl; }

set<set<string>> results;

int match(string pattern, string id) {
    if(pattern.length() != id.length()) {
        return 0;
    }

    for(int i=0; i < pattern.length(); i++) {
        if(pattern[i] != id[i] && pattern[i] != '*') {
            return 0;
        }
    }

    return 1;
}

int backtrack(int i, vector<string> user_id, const vector<string> banned_id, set<string> selected_id) {
    int sum = 0;

    if(i == banned_id.size()) {
        if(results.find(selected_id) == results.end()){
            results.insert(selected_id);
            return 1;
        }
        return 0;
    }

    const string pattern = banned_id[i];

    for(int j=0; j < user_id.size(); j++) {
        string id = user_id[j];
        auto search = selected_id.find(id);
        if(search != selected_id.end()) {
            continue;
        }

        if(match(pattern, id)) {
            selected_id.insert(id);
            sum += backtrack(i + 1, user_id, banned_id, selected_id);
            search = selected_id.find(id);
            selected_id.erase(search);
        }
    }

    return sum;
}

int solution(vector<string> user_id, vector<string> banned_id) {
    set<string> selected_id;
    return backtrack(0, user_id, banned_id, selected_id);
}

int main() {
    vector<string> user_id = {"frodo", "fradi", "crodo", "abc123", "frodoc"};
    vector<string> banned_id = {"fr*d*", "abc1**"};
    cout << (solution(user_id, banned_id) == 2) << '\n';

    // Check whether the solution ignores ordering
    user_id = {"frodo", "fradi", "crodo", "abc123", "frodoc"};
    banned_id = {"*rodo", "*rodo", "******"};
    cout << (solution(user_id, banned_id) == 2) << '\n';
    return 0;
}
