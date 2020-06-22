#include <iostream>
#include <vector>

using namespace std;

#define DEBUG(x) cerr << #x << " = " << x << endl;
#define DEBUGALL(x) { cerr << #x << " = "; for(const auto &e: x) cerr << e << " "; cerr << endl; }

class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        if(nums.size() == 0) {
            return {{}};
        }

        int x = nums.back();
        nums.pop_back();
        vector<vector<int>> v = subsets(nums);

        int N = v.size();
        for(int i=0; i < N; i++) {
            vector<int> u = v[i];
            u.push_back(x);
            v.push_back(u);
        }

        return v;
    }
};

int main() {
    Solution s;
    vector<int> nums = {1,2,3};
    vector<vector<int>> vs = s.subsets(nums);
    for(auto v: vs) {
        DEBUGALL(v);
    }
}
