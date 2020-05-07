import { solution } from './15483'

describe('Edit distance', () => {
  test('insert at the back', () => { expect(solution("abc", "ab")).toBe(1)})
  test('insert at the front', () => { expect(solution("ab", "cab")).toBe(1)})
  test('replace', () => { expect(solution("adc", "abc")).toBe(1)})
  test('', () => { expect(solution("for", "whileforif")).toBe(7)})
  test('', () => { expect(solution("qwerty", "dvorak")).toBe(5)})
})
