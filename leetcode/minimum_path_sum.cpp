#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;
class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int H = grid.size();
        if(H == 0)
            return 0;
        int W = grid[0].size();
        vector<vector<int>> dp(H, vector<int>(W));
        dp[0][0] = grid[0][0];
        for(int i=1; i<W; i++) {
            dp[0][i] = grid[0][i] + dp[0][i-1];
        }

        for(int i=1; i<H; i++) {
            dp[i][0] = grid[i][0] + dp[i-1][0];
        }

        for(int i=1; i<H; i++) {
            for(int j=1; j<W; j++) {
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1]);
            }
        }
        return dp[H-1][W-1];
    }
};

int main() {
    /* 1 3 1
     * 1 5 1
     * 4 2 1
     */
    vector<vector<int>> input{ {1,3,1}, {1,5,1}, {4,2,1} };
    /* 1 2 5
     * 3 2 1
     */
    vector<vector<int>> input2{ {1,2,5}, {3,2,1} };
    cout << Solution().minPathSum(input) << '\n';
    cout << Solution().minPathSum(input2) << '\n';
}
