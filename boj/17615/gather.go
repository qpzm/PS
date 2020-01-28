package main

import "fmt"

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}

func sol(N int, x []int) int {
    var dp = make([][]int, N)
    for i := 0; i < N; i++ {
        for j := 0; j < N; j++ {
            dp[i] = append(dp[i], -1)
        }
    }
    return bulb(0, N-1, x, dp)
}

// dp[i][j] := x[i] 색으로 i~j를 통일하는 최소 횟수
// x[s ~ i], x[i+1 ~ f]로 divide and conquer
// 각 배열의 맨 처음 색이 다르면 1번 추가로 x[i]로 통일
func bulb(s int, f int, x []int, dp [][]int) int {
    INF := int(10e9)
    if dp[s][f] != -1 {
        return dp[s][f]
    }
    if s == f {
        return 0
    }
    dp[s][f] = INF
    for i := s; i < f; i++{
        tmp := bulb(s, i, x, dp) + bulb(i+1, f, x, dp)
        if x[s] != x[i+1] {
            tmp += 1
        }
        if dp[s][f] > tmp {
            dp[s][f] = tmp
        }
    }
    return dp[s][f]
}

func main() {
    var N, K, tmp int
    var x []int
    fmt.Scanf("%d %d", &N, &K)
    for i := 0; i < N; i++ {
        fmt.Scanf("%d", &tmp)
        x = append(x, tmp)
    }
    fmt.Println(sol(N, x))
}
