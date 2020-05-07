import { solution } from './11049'

describe('Parenthesizing matrix multiplication', () => {
  test('(AB)C', () => {
    const input = [[5,3], [3,2], [2,6]];
    const answer = 90;
    expect(solution(input)).toStrictEqual(answer);
  })

  test('AB', () => {
    const input = [[5,3], [3,2]];
    const answer = 30;
    expect(solution(input)).toStrictEqual(answer);
  })

  test('A', () => {
    const input = [[5,3]];
    const answer = 0;
    expect(solution(input)).toStrictEqual(answer);
  })

  test('A(BC)', () => {
    const input = [[3, 2], [2, 6], [6, 5]];
    const answer = 90;
    expect(solution(input)).toStrictEqual(answer);
  })

  test('A(B(CD))', () => {
    const input = [[3, 2], [2, 6], [6, 7], [7, 1]];
    const answer = 60;
    expect(solution(input)).toStrictEqual(answer);
  })
})
