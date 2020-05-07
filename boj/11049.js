function solution(matrices) { // [begin, end]
  const len = matrices.length
  let memo = []
  for(let i=0; i<len; i++) {
    memo.push(Array(len).fill(-1))
  }
  return _sol(matrices, 0, matrices.length - 1, memo)
}

function _sol(matrices, begin, end, memo) {
  if(begin == end) return 0

  if(memo[begin][end] == -1) {
    let min = Infinity
    for(let next_begin=begin+1; next_begin < end + 1; next_begin++) {
      const cur = _sol(matrices, begin, next_begin - 1, memo)
        + _sol(matrices, next_begin, end, memo)
        + matrices[begin][0] * matrices[next_begin][0] * matrices[end][1]
      if(min > cur) {
        min = cur
      }
    }
    memo[begin][end] = min
  }

  return memo[begin][end]
}

function splitAndParse(line) {
  return line.trim().split(/\s+/).map(e => parseInt(e))
}

if (require.main === module) {
  const lines = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n')
  const matrices = []
  var i = 1
  while(i < lines.length) {
    const [M, N] = splitAndParse(lines[i++]).map((s) => parseInt(s))
    matrices.push([M,N])
  }
  console.log(solution(matrices))
}

module.exports = {
  solution: solution
}
