#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    bool isHappy(int n) {
        int m=n, sum=0;
        vector<int> v;

        while(1) {
            v.push_back(m);
            while(m != 0) {
                sum += (m % 10)  * (m % 10);
                m = m / 10;
            }
            if(sum == 1)
                return true;
            if(find(v.begin(), v.end(), sum) != v.end())
                return false;
            m = sum;
            sum = 0;
        }
    }
};

int main() {
    Solution sol;
    assert(sol.isHappy(20) == 0);
    assert(sol.isHappy(19) == 1);
    assert(sol.isHappy(1) == 1);
    assert(sol.isHappy(2) == 0);
    return 0;
}
