#include <iostream>
#include <queue>

using namespace std;
int main() {
    int H, W, max_dist=0, remaining=0;
    cin >> W >> H;
    vector<vector<int>> grid(H, vector<int>(W));

    // Capture all outside vars by reference
    auto inside = [&](int row, int col) {
        return 0 <= row && row < H && 0 <= col && col < W;
    };
    vector<pair<int, int>> directions = {{1,0}, {0,1}, {-1,0}, {0,-1}};
    queue<pair<int, int>> q;

    for(int i = 0; i < H; ++ i)
        for(int j = 0; j < W; ++ j)
            cin >> grid[i][j];

    for(int i = 0; i < H; ++ i) {
        for(int j = 0; j < W; ++ j) {
            if(grid[i][j] == 1)
                q.push({i, j});
        }
    }
    // BFS
    while(q.size() != 0) {
        auto cur = q.front();
        q.pop();
        int dist = grid[cur.first][cur.second];
        max_dist = max(dist, max_dist);
        for (auto dir: directions) {
            int new_row = dir.first + cur.first;
            int new_col = dir.second + cur.second;
            // Not -1: wall and Not 1: visited
            if(inside(new_row, new_col) && grid[new_row][new_col] == 0) {
                q.push({new_row, new_col});
                grid[new_row][new_col] = dist + 1;
            }
        }
    }

    for(int i = 0; i < grid.size(); ++i) {
        for(int j = 0; j < grid[i].size(); ++j) {
            if(grid[i][j] == 0) {
                remaining = 1;
                break;
            }
        }
    }
    if(remaining)
        cout << - 1 << '\n';
    else
        cout << max_dist - 1 << '\n'; // Ripen tomatoes are 1 at day 0
    return 0;
}
