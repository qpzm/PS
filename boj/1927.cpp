#include <iostream>
#include <algorithm>
#include <array>
#define MAX_LEN 100000

using namespace std;

int pop(array<int, MAX_LEN>& heap, int& size) {
    if(size == 0) {
        return 0;
    }
    int res = heap[0];
    heap[0] = heap[size-1];
    size--;
    // Percolate down
    int i = 0;
    while((i+1) * 2 - 1 < size) {
        int lc = (i+1) * 2 - 1;
        int rc = (i+1) * 2;
        int smaller_loc;
        if(rc < size && heap[rc] < heap[lc]) {
            smaller_loc = rc;
        } else {
            smaller_loc = lc;
        }
        if(heap[smaller_loc] < heap[i]) {
            swap(heap[smaller_loc], heap[i]);
            i = smaller_loc;
        }
        else
            break;
    }
    return res;
}

void insert(array<int, MAX_LEN>& heap, int& size, int elem) {
    heap[size] = elem;
    int i = size; // last element is at heap[size]
    // Percolate up
    while(i != 0) {
        int parent = (i-1) / 2;
        if(heap[i] < heap[parent]) {
            swap(heap[parent], heap[i]);
            i = parent;
        }
        else
            break;
    }
    size++;
}

int main() {
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);
    int N, size=0;
    array<int, MAX_LEN> heap;
    cin >> N;

    for(int i = 0; i < N; ++i) {
        int cmd;
        cin >> cmd;
        if(cmd == 0) {
            cout << pop(heap, size) << '\n';
        }
        else {
            insert(heap, size, cmd);
        }
    }
    return 0;
}
