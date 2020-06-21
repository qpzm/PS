#include <string>
#include <vector>

using namespace std;

typedef vector<int> VI;

int solution(vector<VI> board, vector<int> moves) {
    int answer = 0;
    VI stack;

    for(auto m: moves) {
        for(int i = 0; i < board.size(); i++) {
            if(board[i][m - 1] != 0) {
                stack.push_back(board[i][m - 1]);
                board[i][m - 1] = 0;
                break;
            }
        }
        if(1 < stack.size()) {
            int x = stack.back();
            stack.pop_back();
            int y = stack.back();
            if(x == y) {
                stack.pop_back();
                answer += 2;
            } else {
                stack.push_back(x);
            }
        }
    }
    return answer;
}

int main() {
    vector<VI> board = {{0,0,0,0,0},{0,0,1,0,3},{0,2,5,0,1},{4,2,4,4,2},{3,5,1,3,1}};
    VI moves = {1,5,3,5,1,2,1,4};

    assert(solution(board, moves) == 4);

    return 0;
}
