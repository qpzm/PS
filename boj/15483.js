function solution(x, y) {
  const [row, col] = [x.length, y.length]
  const memo = create2dArray(row, col, -1)

  _sol(memo, x, y, 0, 0)
  return memo[0][0]
}

function _sol(memo, x, y, i, j) {
  if(i == x.length) return y.length - j
  if(j == y.length) return x.length - i

  if(memo[i][j] == -1) {
    if(x[i] == y[j]) {
      memo[i][j] = _sol(memo, x, y, i+1, j+1)
    }
    else {
      memo[i][j] = 1 + Math.min(
        _sol(memo, x, y, i+1, j),
        _sol(memo, x, y, i, j+1),
        _sol(memo, x, y, i+1, j+1)
      )
    }
  }
 return memo[i][j]
}

function splitAndParse(line) {
  return line.trim()
}

function create2dArray(row, col, init) {
  let memo = Array(row)
  for (var i = 0; i < row; i++) {
    memo[i] = Array(col).fill(init)
  }
  return memo
}

if (require.main === module) {
  const lines = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n')
  const input = splitAndParse(lines[0])
  const target = splitAndParse(lines[1])
  console.log(solution(input, target))
}

module.exports = {
  solution: solution
}
