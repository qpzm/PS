#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;
vector<int> v;

int find(int x, int start, int end) {
  int len = end - start + 1;
  int half = start + len / 2;

  if(start > end) return 0;
  if(x == v[half]) return 1;
  if(x < v[half]) return find(x, start, half - 1);
  return find(x, half + 1, end);
}

int main() {
  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
  int N, M, x, i;
  cin >> N;
  for(i=0; i<N; i++){
    cin >> x;
    v.push_back(x);
  }

  sort(v.begin(), v.end());

  cin >> M;
  for(i=0; i<M; i++){
    cin >> x;
    cout << find(x, 0, N-1) << '\n' ;
  }
}
