#include <cstdio>
#include <cstdlib>

int comparator(const void *a, const void *b){
  unsigned int *arg1 = (unsigned int*) a;
  unsigned int *arg2 = (unsigned int*) b;
  int result;

  if(arg1[1] > arg2[1])
    result = 1;
  else if(arg1[1] < arg2[1])
    result = -1;
  else{
    if(arg1[0] > arg2[0])
      result = 1;
    else if(arg1[0] < arg2[0])
      result = -1;
    else
      result = 0;
  }
  return result;
}

int main(){
  int n, i, lastFinish = 0, result = 0;
  scanf("%d", &n);
  unsigned int s[n][2];
  for(i=0; i<n; i++){
    scanf("%u %u\n", &s[i][0], &s[i][1]);
  }
  //sort by an increasing order of finishing time
  std::qsort(s, n, sizeof(*s), comparator);

  //calculate the max number of reservation
  i = 0;
  while(i < n){
    if(lastFinish <= s[i][0]){
      result += 1;
      lastFinish = s[i][1];
    }
    i += 1;
  }
  printf("%d\n", result);
}
