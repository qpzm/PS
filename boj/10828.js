class Stack {
  constructor() {
    this.arr = []
  }

  // Assign two pointers -> <-
  push(value) {
    this.arr.push(value)
  }

  pop() {
    if(this.empty()) return -1
    return this.arr.pop()
  }

  size() {
    return this.arr.length
  }

  empty() {
    return this.size() == 0 ? 1 : 0
  }

  top() {
    return this.size() == 0 ? -1 : this.arr[this.size() - 1]
  }
}

function splitAndParse(line) {
  return line.trim().split(/\s+/)
}

if (require.main === module) {
  const lines = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n')
  let msg = "", i = 1
  const q = new Stack()

  while(i < lines.length) {
    var [cmd, val] = splitAndParse(lines[i++])
    if(val === undefined) {
      switch (cmd) {
        case 'pop':
          msg += q.pop() + "\n"
          break;
        case 'size':
          msg += q.size() + "\n"
          break;
        case 'empty':
          msg += q.empty() + "\n"
          break;
        case 'top':
          msg += q.top() + "\n"
          break;
      }
    } else {
      switch (cmd) {
        case 'push':
          q.push(val)
          break;
      }
    }
  }
  console.log(msg)
}
