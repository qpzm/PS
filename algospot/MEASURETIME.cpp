#include <bits/stdc++.h>
#define MAX_ELEM 999999
using namespace std;

class FenwickTree {
    private:
        vector<int> tree;

    public:
        FenwickTree(int n) : tree(n+1) {}

        int sum(int pos) {
            ++pos; // pos in [1, n+1)
            int ret = 0;
            // 1100
            while(pos > 0) { // not use index 0
                ret += tree[pos];
                pos &= pos - 1; // find the next leftmost one
            }

            return ret;
        }

        void add(int pos, int val) {
            ++pos;
            while(pos < tree.size()) {
                tree[pos] += val;
                pos += pos & -pos; // add the rightmost one
            }
        }
};

long long countMoves(const vector<int>& A) {
    long long ret = 0;
    FenwickTree tree(MAX_ELEM + 1); // [0, MAX_ELEM]
    for(int i = 0; i < A.size(); ++i) {
        ret += tree.sum(MAX_ELEM) - tree.sum(A[i]); // Count # of elements > A[i]
        tree.add(A[i], 1);
    }
    return ret;
}

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    int C, N, num;
    scanf("%d", &C);
    while(C--) {
        vector<int> v;
        scanf("%d", &N);
        while(N--) {
            scanf("%d", &num);
            v.push_back(num);
        }

        printf("%lld\n", countMoves(v));
    }
    return 0;
}
