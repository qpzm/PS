package main
import ("fmt")

func Abs(x int) int {
  if (x < 0) {
    return -x
  }
  return x
}

func main() {
  var n int
  fmt.Scanf("%d", &n)
  n = n - 1
  for i := 0; i < 2*n+1; i++ {
    k := n - Abs(i - n)
    for j := 0; j <= k; j++ {
      fmt.Print("*")
    }
    for j := 0; j < 2*(n-k); j++ {
      fmt.Print(" ")
    }
    for j := 0; j <= k; j++ {
      fmt.Print("*")
    }
    fmt.Println()
  }
}
