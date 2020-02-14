#include <iostream>
#include <vector>
#include <cassert>
using namespace std;
#define SIZE 9
typedef pair<int,int> Point;
typedef vector<Point>::iterator Iterator;

int map[SIZE][SIZE];
bool DONE=false;
vector<Point> v;

bool valid();
void parse_input();
void print_output();
void solve(Iterator);
void check();

int main(){
  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
  parse_input();
  solve(v.begin());
  check();
  print_output();
}

void check() {
  int i,j;
  int cnt[9] = {0};
  for (i=0; i < SIZE; i++) {
    for (j=0; j < SIZE; j++) {
      cnt[map[i][j] - 1]++;
    }
  }

  for (i=0; i < SIZE; i++) {
    assert(cnt[i] == SIZE);
  }
}

bool valid(int i, int j, int num) {
  int area_i = 3*(i / 3), area_j = 3*(j / 3);

  for(int k=0; k<SIZE; k++) {
    if(map[i][k] == num || map[k][j] == num) return false;
  }

  for(int a=0; a<3; a++) {
    for(int b=0; b<3; b++) {
      if(map[area_i + a][area_j + b] == num) {
        //cout << "Visit" <  << "," << j << " : " << n << endl;
        return false;
      }
    }
  }

  return true;
}

void parse_input() {
  int n;
  for (int i=0; i <SIZE; i++) {
    for (int j=0; j < SIZE; j++) {
      cin >> n;
      map[i][j] = n;
      if(n == 0) v.push_back(make_pair(i, j));
    }
  }
}

void print_output() {
  int i,j;
  for (i=0; i < SIZE; i++) {
    for (j=0; j < SIZE-1; j++) {
      cout << map[i][j] << ' ';
    }
    cout << map[i][j] << '\n';
  }
}

void solve(Iterator it) {
  if(it == v.end()) {
    DONE = true;
    return;
  }

  int i = it->first;
  int j = it->second;

  for (int n=1; n <= 9; n++) {
    if(valid(i, j, n)) {
      map[i][j] = n;
      solve(next(it));
      if(DONE) break;
      else map[i][j] = 0;
    }
  }
}
