import {solution} from './failure'

test('Basic', () => {
  expect(solution(2, [1, 2])).toStrictEqual([2, 1])
})

test('N+1', () => {
  expect(solution(3, [4])).toStrictEqual([1,2,3])
})

test('Example1', () => {
  expect(solution(5, [2, 1, 2, 6, 2, 4, 3, 3])).toStrictEqual([3,4,2,1,5])
})

test('Example2', () => {
  expect(solution(4, [4,4,4,4,4])).toStrictEqual([4,1,2,3])
})
