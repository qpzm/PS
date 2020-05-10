import { solution } from './chat'

describe('', () => {
  test('Example1', () => {
    const input = [
      "Enter uid1234 Muzi",
      "Enter uid4567 Prodo",
      "Leave uid1234",
      "Enter uid1234 Prodo",
      "Change uid4567 Ryan"
    ]
    const answer = [
      "Prodo님이 들어왔습니다.",
      "Ryan님이 들어왔습니다.",
      "Prodo님이 나갔습니다.",
      "Prodo님이 들어왔습니다.",
    ]
    expect(solution(input)).toStrictEqual(answer);
  })

  test('Example2', () => {
    const input = [
      "Enter uid1234 Muzi",
      "Enter uid4567 Prodo",
      "Enter uid2345 Prodo",
      "Leave uid1234",
      //"Enter uid1234 Prodo",
      //"Change uid4567 Ryan"
    ]
    const answer = [
      "Muzi님이 들어왔습니다.",
      "Prodo님이 들어왔습니다.",
      "Prodo님이 들어왔습니다.",
      "Muzi님이 나갔습니다.",
    ]
    expect(solution(input)).toStrictEqual(answer);
  })
})
