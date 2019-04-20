#include <stdio.h>
#include <string.h>
#define max(x,y) (((x) > (y)) ? (x) : (y))

// N^2 solution
int lds(int* num, int* mem, int i) {
  int res, tmp, longest_len = 1;
  if(mem[i] != 0) res = mem[i];
  else {
    for(int j=i-1; j > -1; j--) {
      tmp = lds(num, mem, j);
      if(num[j] > num[i] && longest_len < (1+tmp))
        longest_len = 1+tmp;
    }
    res = longest_len;
  }
  mem[i] = res;
  return res;
}

int main() {
  int N;
  scanf("%d", &N);
  int num[N], longest, longest_end_here[N];
  for(int i=0; i<N; i++) scanf("%d", num+i);
  memset(longest_end_here, 0, N * sizeof(int));
  longest_end_here[0] = 1;

  lds(num, longest_end_here, N-1);
  longest = longest_end_here[0];

  for (int i = 1; i < N; i++)
    if (longest_end_here[i] > longest)
       longest  = longest_end_here[i];

  printf("%d", longest);
  return 0;
}
