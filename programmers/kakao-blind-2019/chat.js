function solution(record) {
  let answer = []
  const uid_to_name = new Map()

  record.forEach((line) => {
    const [cmd, uid, name] = line.trim().split(/\s+/)
    if(cmd == "Enter") {
      uid_to_name.set(uid, name)
      answer.push([uid, "님이 들어왔습니다."])
    } else if(cmd == "Leave") {
      answer.push([uid, "님이 나갔습니다."])
    } else if(cmd == "Change") {
      uid_to_name.set(uid, name)
    }
  })

  return answer.map((item) => {
    const uid = item[0]
    const name = uid_to_name.get(uid)
    return name + item[1]
  })
}

function enter(hash, uid, name) {
  hash[uid] = name
}

function leave(hash, uid) {
  hash[uid] = name
}

// 기존에 채팅방에 출력되어 있던 메시지의 닉네임도
// 전부 변경된다.
function change(hash, uid, name) {
  hash[uid] = name
}

function create2dArray(row, col, init) {
  let memo = Array(row)
  for (var i = 0; i < row; i++) {
    memo[i] = Array(col).fill(init)
  }
  return memo
}

module.exports = {
  solution: solution
}
