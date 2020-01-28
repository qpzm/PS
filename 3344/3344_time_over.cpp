#include <iostream>
#include <cstring>
using namespace std;

bool done = false;
bool is_safe(int arr[], int size, int row, int col) {
  for(int i = 0; i < col; i++) {
    int row2 = arr[i];
    if(row == row2 || (row - row2) == (col - i) || (row2 - row) == (col - i)) {
      return false;
    }
  }
  return true;
}

void n_queen_iter(int arr[], int size, int col) {
  for(int row = 0; row < size; row++){
    if(is_safe(arr, size, row, col)){
      arr[col] = row;
      if(col == size - 1){
        done = true;
      } else {
        n_queen_iter(arr, size, col + 1);
        if(done) break;
        arr[col] = -1;
      }
    }
  }
}

int* n_queen(int arr[], int size) {
  n_queen_iter(arr, size, 0);
  return arr;
}

int main(){
  int size;
  cin >> size;
  int arr[size];
  memset(arr, -1, sizeof(int) * size);
  n_queen(arr, size);
  for(int i=0; i < size; i++) { cout << arr[i] << endl; }
  return 0;
}
