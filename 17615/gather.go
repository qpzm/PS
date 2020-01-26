package main

import "fmt"

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}

func bulb(l int, x []int) int {
    memo := make([][]int, l)
    for i := 0; i < l; i++ {
        for j := 0; j < l; j++ {
            memo[i] = append(memo[i], 0)
        }
    }
    for i := 0; i < l-1; i++ {
        if x[i] != x[i+1] {
            memo[i][i+1] = 1
        } else {
            memo[i][i+1] = 0
        }
    }
    for diff := 2; diff < l; diff++ {
        for row := 0; row < l-diff; row++ {
            col := row + diff
            if x[row] == x[row+1] {
                memo[row][col] = memo[row+1][col]
            } else if x[col] == x[col-1]{
                memo[row][col] = memo[row][col-1]
            } else if x[row] == x[col] {
                memo[row][col] = 1 + memo[row+1][col-1]
            } else {
                memo[row][col] = 1 + min(memo[row][col-1], memo[row+1][col])
            }
        }
    }
    return memo[0][l-1]
}

func main() {
    var N, K, tmp int
    var a []int
    fmt.Scanf("%d %d", &N, &K)
    for i := 0; i < N; i++ {
        fmt.Scanf("%d", &tmp)
        a = append(a, tmp)
    }
    fmt.Println(bulb(N, a))
}
