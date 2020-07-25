#include <vector>
#include <string>
#include <iostream>
#include <algorithm>

using namespace std;

typedef vector<int> VI;

#define SCORE_MAX 1000000; // Loose bound max_len * max_score of a chunk

VI split(string s) {
    VI v;
    for(char c: s) {
        v.push_back((int) c - (int) '0');
    }

    return v;
}

int calc_score(VI &v, int start, int end) { // [start, end)
    int first = v[start];
    int second = v[start + 1];

    // 1. All Equal
    bool res = true;
    for(int i = start + 1; i < end; ++i) {
        res = res && (v[i] == first);
    }
    if(res) return 1;

    // 2-1. 1씩 단조 증가
    res = true;
    for(int i = start + 1; i < end; ++i) {
        res = res && (v[i] - v[i -1]) == 1;
    }
    if(res) return 2;

    // 2-2. 1씩 단조 감소
    res = true;
    for(int i = start + 1; i < end; ++i) {
        res = res && (v[i] - v[i -1]) == -1;
    }
    if(res) return 2;

    // 3. Alternating
    res = true;
    for(int i = start + 2; i < end; ++i) {
        res = res && v[i] == v[i - 2];
    }
    if(res) return 4;

    // 4. Arithmetic sequence(등차수열)
    int diff = second - first;
    res = true;
    for(int i = start + 2; i < end; ++i) {
        res = res && (v[i] - v[i -1]) == diff;
    }
    if(res) return 5;

    return 10;
}

int dp(VI &v, VI &scores, int start) {
    int min_score;

    if(start == v.size()) {
        return 0;
    }

    if(v.size() - 3 < start) {
        return SCORE_MAX;
    }

    if(scores[start] != 0) {
        return scores[start];
    }

    min_score = SCORE_MAX;
    for(int offset = 3; offset < 6; offset++) {
        int end = start + offset;
        int cur_score = calc_score(v, start, end);
        min_score = min(min_score, cur_score + dp(v, scores, end));
    }
    scores[start] = min_score;
    return min_score;
}

int main() {
    ios_base::sync_with_stdio(false);
	cin.tie(NULL);

    int n, x;
    string s;
    cin >> n;

    for(int i = 0; i < n; ++i) {
        cin >> s;
        VI v = split(s);
        VI scores(v.size(), 0);
        // Def. score[i] = i부터 시작하는 수열의 최소 난이도
        cout << dp(v, scores, 0) << '\n';
    }

    return 0;
}
