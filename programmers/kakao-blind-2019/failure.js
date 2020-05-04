// N stages: 1 ~ N
// N + 1: The user cleared all stages
// If no one reaches the stage, the rate is 0
// Return stage# order by (faliure desc, stage# inc)

function solution(N, stages) {
  // fail / pass
  let counts = Array(N+2).fill(0)
  stages.forEach((stage) => {
    counts[stage] += 1
  })

  let total = counts[N+1]
  let answer = Array(N).fill(0)
  for(let stage = N; stage > 0; stage--) {
    total += counts[stage]
    answer[stage-1] = { 'stage': stage, 'rate': counts[stage] / total }
  }

  return answer.sort(compare).map((item) => (item.stage))
}

function compare(a, b) {
  if(a.rate > b.rate) {
    return -1
  }
  if(a.rate < b.rate) {
    return 1
  }
  return a.stage - b.stage
}

module.exports = {
  solution: solution
}
