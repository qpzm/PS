#include <vector>
#include <iostream>
using namespace std;

int min_coins(const vector<int> coins, const int target) {
    // 0 <= row <= target
    int H = coins.size(), W = target + 1;
    vector<vector<int>> dp(H, vector<int>(W, -1));
    for(int i=0, coin=coins[0]; coin * i < W; i++){
        dp[0][coin * i] = i;
    }

    for(int i = 1; i < H; ++i) {
        int coin = coins[i];
        for(int j=0; j < W; ++j){
            for(int k=0; 0 <= j - coin * k; k++){
                int prev = dp[i-1][j - coin*k];
                if(prev != -1) {
                    if(dp[i][j] == -1)
                        dp[i][j] = k + prev;
                    else if(dp[i][j] > k + prev)
                        dp[i][j] = k + prev;
                }
            }
        }
    }

    return dp[H-1][W-1];
}

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    int N, K, num;
    vector<int> coins;
    cin >> N >> K;
    for(int i = 0; i < N; ++i) {
        cin >> num;
        coins.push_back(num);
    }
    int res = min_coins(coins, K);
    cout << res << '\n';
    return 0;
}
