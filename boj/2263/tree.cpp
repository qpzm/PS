#include <vector>
#include <iostream>
using namespace std;

#define REP(i, n) for(int i = 0; i < (int)(n); ++ i)
#define FOR(i, b, e) for(auto i = b; i < e; ++ i)
#define all(x) (x).begin(), (x).end()

vector<int> inorder, postorder;
void preorder(const int in_begin, const int post_begin, const int len) {
    int i, root_index, root, left_len, right_len;
    if(len == 0) return;

    root = postorder[post_begin + len - 1];
    FOR(i, in_begin, in_begin+len) {
        if(inorder[i] == root) {
            root_index = i;
            break;
        }
    }

    left_len = root_index - in_begin;
    right_len = len - left_len - 1;

    cout << root << ' ';
    preorder(in_begin, post_begin, left_len);
    preorder(root_index + 1, post_begin + left_len, right_len);
}

int main() {
    ios::sync_with_stdio(false);
	cin.tie(0);
    int i, N, k;
    cin >> N;

    REP(i, N) {
        cin >> k;
        inorder.push_back(k);
    }

    REP(i, N) {
        cin >> k;
        postorder.push_back(k);
    }

    preorder(0, 0, N);
}
