#include <string>
#include <vector>
#include <set>
#include <cctype>
#include <algorithm>
#include <iostream>

using namespace std;

#define DEBUG(x) cerr << #x << " = " << x << endl;
#define DEBUGALL(x) { cerr << #x << " = "; for(const auto &e: x) cerr << e << " "; cerr << endl; }

bool compare(vector<int> x, vector<int> y) {
    return (x.size() < y.size());
}

class Parser {
    public:
        int stage = 0;
        vector<vector<int>> items;

        void parse(string s) {
            int pos = 0;
            while(pos != s.size()) {
                if(pos == s.size()) return;
                char c = s[pos];
                if(c == '{') {
                    if(stage == 1) {
                        items.push_back({});
                    }
                    stage++;
                } else if(c == '}') {
                    stage--;
                } else if(c == ',') {

                } else { // int
                    int pos2 = pos;
                    while(isdigit(s[pos2])) pos2++;
                    pos2--;
                    int n = stoi(s.substr(pos, pos2 - pos + 1));
                    pos = pos2;
                    items.back().push_back(n);
                }
                pos++;
            }
        }

        vector<int> make_tuple() {
            vector<int> answer;
            set<int> s;
            sort(items.begin(), items.end(), compare);
            for(auto l: items) {
                for(auto x: l) {
                    if(s.find(x) == s.end()) {
                        s.insert(x);
                        answer.push_back(x);
                        break;
                    }
                }
            }
            return answer;
        }

};

vector<int> solution(string s) {
    Parser p;
    p.parse(s);
    return p.make_tuple();
}

int main() {
    string s = "{{2},{2,1},{2,1,3},{2,1,3,4}}";
    vector<int> answer = {2,1,3,4};
    DEBUGALL(solution(s));
    assert(solution(s) == answer);

    s = "{{1,2,3},{2,1},{1,2,4,3},{2}}";
    answer = {2, 1, 3, 4};
    assert(solution(s) == answer);

    s = "{{123}}";
    answer = {123};
    assert(solution(s) == answer);
}
