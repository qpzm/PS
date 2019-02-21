#include <iostream>

using namespace std;
int max(int[], int);
int lis(int arr[], int size){
  int memo[size];
  for(int i=0; i<size; i++){
    memo[i] = 0;
  }
  for(int i=0; i<size; i++){
    for(int j=0; j<i; j++){
      if(arr[i] > arr[j] && memo[i] < memo[j] + 1)
        memo[i] = memo[j] + 1;
    }
  }
  return max(memo, size) + 1; //since initialized in 0
}

int main(){
  int size;
  cin >> size;
  int arr[size];
  for(int i=0; i< size; i++){
    cin >> arr[i];
  }
  cout << lis(arr, size);
  return 0;
}


int max(int arr[], int size){
  int result = arr[0];
  for(int i=1; i< size; i++){
   if(result < arr[i])
      result = arr[i];
  }
  return result;
}
