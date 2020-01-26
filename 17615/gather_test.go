package main

import "testing"

func TestSol(t *testing.T) {
    cases := []struct {
        n int
        in []int
        want int
    }{
        {1, []int{1}, 0},
        {3, []int{1, 2, 1}, 1},
        {3, []int{1, 1, 2}, 1},
        {4, []int{1, 2, 1, 2}, 2},
        {5, []int{1, 2, 1, 2, 1}, 2},
        {6, []int{1, 2, 1, 2, 1, 3}, 3},
        {5, []int{1, 2, 4, 2, 1}, 2},
        {5, []int{1, 2, 4, 3, 1}, 3},
        {8, []int{1, 2, 4, 3, 1, 2, 1, 3}, 5},
        {8, []int{1, 2, 3, 7, 1, 8, 6, 8}, 5},
        {10, []int{1, 1, 2, 3, 3, 3, 2, 2, 1, 1}, 2},
    }
    for _, c := range cases {
        got := sol(c.n, c.in)
        if got != c.want {
            t.Errorf("sol(%d) == %d, want %d", c.in, got, c.want)
        }
    }
}
