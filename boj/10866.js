class Node {
  constructor(value=null, prev=null, next=null) {
    this.value = value
    this.prev = prev
    this.next = next
  }
}

class Deque {
  constructor() {
    this.front = null
    this.back = null
    this.size = 0
  }

  // Assign two pointers -> <-
  pushFront(value) {
    const node = new Node(value, null, this.front)
    if(this.empty()) {
      this.front = node
      this.back = node
    } else {
      this.front.prev = node
      this.front = node
    }
    this.size += 1
  }

  popFront() {
    if(this.empty()) return -1
    if(this.size == 1) {
      this.back = null
    }

    const node = this.front
    this.front = this.front.next
    this.size -= 1
    return node.value
  }

  pushBack(value) {
    const node = new Node(value, this.back, null)
    if(this.empty()) {
      this.front = node
      this.back = node
    } else {
      this.back.next = node
      this.back = node
    }
    this.size += 1
  }

  popBack() {
    if(this.empty()) return -1

    if(this.size == 1) {
      this.front = null
    }

    const node = this.back
    this.back = this.back.prev
    this.size -= 1
    return node.value
  }

  empty() {
    return this.size == 0 ? 1 : 0
  }

  peepFront() {
    return this.size == 0 ? -1 : this.front.value
  }

  peepBack() {
    return this.size == 0 ? -1 : this.back.value
  }
}

function splitAndParse(line) {
  return line.trim().split(/\s+/)
}

if (require.main === module) {
  const lines = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n')
  let i = 1, msg = ""
  const q = new Deque()

  while(i < lines.length) {
    var [cmd, val] = splitAndParse(lines[i++])
    if(val === undefined) {
      switch (cmd) {
        case 'pop_back':
          msg += q.popBack() + "\n"
          break;
        case 'pop_front':
          msg += q.popFront() + "\n"
          break;
        case 'size':
          msg += q.size + "\n"
          break;
        case 'empty':
          msg += q.empty() + "\n"
          break;
        case 'front':
          msg += q.peepFront() + "\n"
          break;
        case 'back':
          msg += q.peepBack() + "\n"
          break;
      }
    } else {
      switch (cmd) {
        case 'push_back':
          q.pushBack(val)
          break;
        case 'push_front':
          q.pushFront(val)
          break;
      }
    }
  }
  process.stdout.write(msg)
}

module.exports = { Deque }
