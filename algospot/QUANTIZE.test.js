import {solve, naive} from './QUANTIZE.js'

describe('when S >= N returns 0', () => {
  test.only('S=2, N=1', () => {
    const input = [9]
    expect(solve(input, 2, 1)).toStrictEqual(0);
  })

  test.only('S=3, N=2', () => {
    const input = [8, 9]
    expect(solve(input, 3, 2)).toStrictEqual(0);
  })

  test.only('S=2, N=2', () => {
    const input = [8, 9]
    expect(solve(input, 2, 2)).toStrictEqual(0);
  })
})

test('test0', () => {
  const input = [1, 2, 3, 4]
  expect(solve(input, 4, 4)).toStrictEqual(0);
})

// No need to be contiguous
test('test1', () => {
  const input = [ 3, 3, 3, 1, 2, 3, 2, 2, 2, 1 ].sort()
  expect(solve(input, 3, 10)).toStrictEqual(0);
})

test('test2', () => {
  const input = [ 1, 2, 3, 4, 5, 6 ]
  expect(solve(input, 3, 6)).toStrictEqual(3);
})

test('test3', () => {
  const input = [ 1, 744, 755, 4, 897, 902, 890, 6, 777 ].sort()
  expect(solve(input, 3, 9)).toStrictEqual(651);
})

test('test4', () => {
  const input = [ 1,2,3 ]
  expect(solve(input, 1, 3)).toStrictEqual(2);
})

test('test5', () => {
  const input = [ 1,2,3,4 ]
  expect(solve(input, 2,4)).toStrictEqual(2);
})

test('test6', () => {
  const input = [ 1,2,3,4,5,6,7,8,9,10,11 ]
  expect(solve(input, 3, 11)).toStrictEqual(14);
})

test('test8', () => {
  const input = [1]
  expect(solve(input, 1, 1)).toStrictEqual(0);
})

describe('naive', () => {
  test('test1', () => {
    const input = [ 1,2,3 ]
    expect(naive(input, 1, 3)).toStrictEqual(2);
  })

  // No need to be contiguous
  test('test1', () => {
    const input = [ 3, 3, 3, 1, 2, 3, 2, 2, 2, 1 ].sort()
    expect(naive(input, 3, 10)).toStrictEqual(0);
  })

  test('test2', () => {
    const input = [ 1, 2, 3, 4, 5, 6 ]
    expect(naive(input, 3, 6)).toStrictEqual(3);
  })

  test('test3', () => {
    const input = [ 1, 744, 755, 4, 897, 902, 890, 6, 777 ].sort()
    expect(naive(input, 3, 9)).toStrictEqual(651);
  })

  test.only('all', () => {
    let nums = []
    for(let i = 1; i < 11; ++i) {
      nums.push(i)
    }

    for(let S = 1; S < 10; ++S) {
      for(let i = 0; i < 10; ++i) {
        for(let j = i; j < 11; ++j) {
          const input = nums.slice(i, j)
          console.log(input)
/*          const N = input.length*/
          //const ans1 = naive(input, S, N), ans2 = solve(input, S, N)
          //if(ans1 != ans2) {
            //console.log(input, S, N, ans1, ans2)
            //break
          /*}*/
        }
      }
    }
  })

  test.skip('random', () => {
    var times = 100;
    for(var i=0; i < times; i++){
      const S = 10, N = 100
      const input = Array.from({length: N}, () => Math.floor(Math.random() * 1000))
      input.sort()
      const ans1 = naive(input, S, N), ans2 = solve(input, S, N)
      console.log(input, ans1, ans2)
      expect(ans1).toStrictEqual(ans2)
    }
  })
})
