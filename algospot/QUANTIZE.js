/* Array.prototype.sort() sort according to each character's Unicode code point value.
 * To sort integer array, give optional compare function.
 *
 * const array1 = [1, 30, 4, 21, 100000];
 * array1.sort();
 * console.log(array1); // => Array [1, 100000, 21, 30, 4]
 */

const lines = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n')
let i = 1

while(i < lines.length) {
  let [N, S] = splitAndParse(lines[i++])
  let input_seq = splitAndParse(lines[i++]).sort(compare)
  console.log(solve(input_seq, S, N))
}

function solve(input_seq, S, N) {
  if(N <= S) {
    return 0
  }

  let memo = create2dArray(S, N)

  for (let i = 0; i < memo.length; i++) { // i: # of partition - 1
    for (let j = i; j < memo[0].length; j++) { // j: inclusive end of input_seq
      if(j == i) {
        memo[i][j] = 0
      } else if(i == 0) {
        memo[i][j] = min_square_error(input_seq, i, j + 1)
      } else {
        // base = f(i-1, i-1) + input_seq[i, j + 1)
        memo[i][j] = Infinity
        for(let k=i-1; k < j + 1; k++) {
          memo[i][j] = Math.min(memo[i-1][k] + min_square_error(input_seq, k + 1, j+1), memo[i][j])
        }
      }
    }
  }

  return(memo[S-1][N-1])
}

function compare(a, b) {
  if (a < b) {
    return -1;
  }
  if (a > b) {
    return 1;
  }
  return 0;
}

function naive(input_seq, S, N) {
  return _naive(input_seq, 0, N, S)
}

function _naive(input_seq, start, end, S) {
  const len = end - start
  if(len <= S) {
    return 0
  } else if(S == 1) {
    return min_square_error(input_seq, start, end)
  }
  else{
    let base = Infinity
    for(let i=start; i + 1 < end; i++) {
      base = Math.min(min_square_error(input_seq, start, i+1) +
        _naive(input_seq, i+1, end, S - 1), base)
    }
    return base
  }
}

// [start, end)
function min_square_error(arr, start, end) {
  const avg = int_average(arr, start, end)
  let error = 0;
  for(let i=start; i < end; i++) {
    error += square_error(arr[i], avg)
  }
  return error
}

// [start, end)
function int_average(arr, start, end) {
  if(start >= end) {
    return NaN
  }
  let sum = 0
  for(let i=start; i < end; i++) {
    sum += arr[i]
  }
  return Math.round(sum / (end-start))
}

function square_error(x, m) {
  return (x - m) * (x - m)
}

function splitAndParse(line) {
  return line.trim().split(/\s+/).map(e => parseInt(e))
}

function create2dArray(H, W) {
  var x = new Array(H);
  for (var i = 0; i < H; i++) {
    x[i] = new Array(W);
  }
  return x
}

module.exports = {
  solve: solve,
  naive: naive
}
