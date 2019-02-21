#include <cstdio>
using namespace std;

int makeMultiple(int n, int divisor) {
  //Calculate min by subracting the first two digits
  int result;
  int min = n - (n%100);
  int quotient = min/divisor;
  int remainder = min%divisor;
  // add deficiency to make the min multiple
  if(remainder == 0){
    result = min;
  }
  else{
    result = min + (divisor - remainder);
  }
  return result;
}

int main() {
  int n, divisor;
  scanf("%d\n%d", &n, &divisor);
  //print last two digits with zero padding
  printf("%02d\n", makeMultiple(n, divisor)%100);
}
