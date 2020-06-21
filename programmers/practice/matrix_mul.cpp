#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;
#define MAX_LEN 200

int solution(vector<vector<int>> matrix_sizes) {
    int memo[MAX_LEN][MAX_LEN] = {0}; // min of multiplying matrices in [start, end]
    int n = matrix_sizes.size();
    int end;

    for(int diff=1; diff<n; diff++) {
        for(int start=0; start<(n-diff); start++) {
            end = start + diff;
            for(int i=start; i < end; i++) {
                int local_sum = memo[start][i] + memo[i+1][end] +
                    matrix_sizes[start][0] * matrix_sizes[i][1] * matrix_sizes[end][1];
                if(memo[start][end] == 0 || memo[start][end] > local_sum) {
                    memo[start][end] = local_sum;
                }
            }
        }
    }

    return memo[0][n - 1];
}

int main() {
    vector<vector<int>> matrix_sizes = {{5,3}, {3,10}, {10,6}}; // min: A(BC)
    cout << solution(matrix_sizes) << endl;
    matrix_sizes = {{5,3}, {3,2}, {2,6}, {6, 3}}; // min: (AB)(CD)
    cout << solution(matrix_sizes) << endl;
}
