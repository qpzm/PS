 #include <stdio.h>

 void hanoi(int n, int src, int middle, int dest);
 int hanoi_count(int n);

 int main() {
     int i;
     scanf("%d", &i);
     printf("%d\n", hanoi_count(i));
     hanoi(i, 1, 2, 3);

     return 0;
 }

 int hanoi_count(int n){
     if (n == 1)
         return 1;

     return hanoi_count(n-1) *2 +1;
 }

 void hanoi(int n, int src, int middle, int dest) {
     if (n == 1) {
         printf("%d %d\n", src, dest);
     } else {
         hanoi(n-1, src, dest, middle);
         printf("%d %d\n", src, dest);
         hanoi(n-1, middle, src, dest);
     }
 }
