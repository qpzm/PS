#include <iostream>
//#include <cstring>
using namespace std;

int sum = 0;

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
      if(col == size - 1){
        sum += 1;
      } else {
        arr[col] = row;
        n_queen_iter(arr, size, col + 1);
        //arr[col] = -1;
      }
    }
  }
}

void n_queen(int size) {
  int arr[size];
  //memset(arr, -1, sizeof(int) * size);
  n_queen_iter(arr, size, 0);
}

int main(){
  int size;
  cin >> size;
  n_queen(size);
  cout << sum << endl;
  return 0;
}
