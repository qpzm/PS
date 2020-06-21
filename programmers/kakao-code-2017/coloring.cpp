#include <vector>
#include <iostream>

using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int, int> PII;

#define DEBUG(x) cerr << #x << " = " << x << endl;
#define DEBUGALL(x) { cerr << #x << " = "; for(const auto &e: x) cerr << e << " "; cerr << endl; }

int visited[100][100];

int dfs(int m, int n, int color, VVI picture) {
    int M = picture.size();
    int N = picture[0].size();
    int sum = 1;
    vector<PII> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    for(auto p: directions) {
        int new_m = m + p.first;
        int new_n = n + p.second;
        if(0 <= new_m && new_m < M && 0 <= new_n && new_n < N &&
                picture[new_m][new_n] == color && !visited[new_m][new_n]) {
            visited[new_m][new_n] = 1;
            sum += dfs(new_m, new_n, color, picture);
        }
    }

    return sum;
}

// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
VI solution(int M, int N, VVI picture) {
    int number_of_area = 0;
    int max_size_of_one_area = 0;
    VI answer(2);

    for(int i = 0; i < M; ++i) {
        for(int j = 0; j < N; ++j) {
            visited[i][j] = 0;
        }
    }

    for(int i = 0; i < M; ++i) {
        for(int j = 0; j < N; ++j) {
            if(!visited[i][j] && picture[i][j] != 0) {
                int color = picture[i][j];
                visited[i][j] = 1;
                number_of_area += 1;
                int area = dfs(i, j, color, picture);
                if(area > max_size_of_one_area) {
                    max_size_of_one_area = area;
                }
            }
        }
    }

    answer[0] = number_of_area;
    answer[1] = max_size_of_one_area;
    return answer;
}

int main() {
    VVI picture = {{1, 1, 1, 0}, {1, 2, 2, 0}, {1, 0, 0, 1}, {0, 0, 0, 1}, {0, 0, 0, 3}, {0, 0, 0, 3}};
    VI answer = solution(6, 4, picture);
    DEBUGALL(answer)
}
