#include <cstdio>
#include <vector>

using namespace std;

int main() {
    char input[101];
    vector<int> stack;
    int res = 1;
    scanf("%s", input);
    for(int i=0;input[i] != '\0';i++) {
        stack.push_back(input[i]);
    }
    for(int i=0;input[i] != '\0';i++) {
        if(input[i] != stack.back()) {
            res = 0;
            break;
        }
        stack.pop_back();
    }
    printf("%d\n", res);
}
