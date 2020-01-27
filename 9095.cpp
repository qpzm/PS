#include <cstdio>

/*
0 0 1
0 1 1
1 1 2
1 2 4
2 4 7
*/
int sol(int x){
    int a=0, b=0, c=1, tmp;
    for(int i=0; i < x; i++){
        tmp = c;
        c = a + b + c;
        a = b;
        b = tmp;
    }
    return c;
}

int main() {
    int N, x;
    scanf("%d", &N);
    for(int i=0; i<N; i++){
        scanf("%d", &x);
        printf("%d\n", sol(x));
    }
}
