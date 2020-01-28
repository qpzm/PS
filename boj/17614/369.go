package main

import (
    "fmt"
)

func calculate(n int) int {
    cnt := 0
    for i := 1; i <= n; i++ {
        j := i
        for j > 0 {
            cur := (j % 10)
            if cur % 3 == 0 && cur != 0 {
                cnt += 1
            }
            j /= 10
        }
    }
    return cnt
}

func main() {
    var input int
    fmt.Scanf("%d", &input)
    fmt.Print(calculate(input))
}
