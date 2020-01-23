package main

import "testing"

func Test369(t *testing.T) {
    cases := []struct {
        in, want int
    }{
        {1, 0},
        {3, 1},
        {12, 3},
        {14, 4},
        {36, 18},
        {37, 19},
    }
    for _, c := range cases {
        got := calculate(c.in)
        if got != c.want {
            t.Errorf("Calculate(%d) == %d, want %d", c.in, got, c.want)
        }
    }
}
