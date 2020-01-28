#include <cstdio>

int main() {
    int N, a=1, b=1, tmp;
    scanf("%d", &N);
    for(int i=1; i<N; i++) {
        tmp = b;
        b = (2 * a + b) % 10007;
        a = tmp;
    }
    printf("%d\n", b);
}
