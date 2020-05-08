import { Deque } from './10866'

describe('Deque', () => {
  test('back', () => {
    const q = new Deque()
    q.pushBack(2)
    expect(q.size).toBe(1);
    expect(q.peepBack()).toBe(2);
    expect(q.peepFront()).toBe(2);

    expect(q.popBack()).toBe(2);
    expect(q.size).toBe(0);
  })

  test('front', () => {
    const q = new Deque()
    q.pushFront(2)
    expect(q.size).toBe(1);
    expect(q.peepBack()).toBe(2);
    expect(q.peepFront()).toBe(2);

    expect(q.popFront()).toBe(2);
    expect(q.size).toBe(0);
  })

  test('Size 2 -> 1 and peepFront', () => {
    const q = new Deque()
    q.pushFront(2)
    q.pushBack(3)
    expect(q.size).toBe(2);
    expect(q.popFront()).toBe(2);
    expect(q.peepFront()).toBe(3);
  })

  test('Size 2 -> 1 and peepBack', () => {
    const q = new Deque()
    q.pushFront(2)
    q.pushBack(3)
    expect(q.size).toBe(2);
    expect(q.popBack()).toBe(3);
    expect(q.peepBack()).toBe(2);
  })

  test('Size 1 -> 0 and peepBack', () => {
    const q = new Deque()
    q.pushFront(2)
    expect(q.popBack()).toBe(2)
    expect(q.peepBack()).toBe(-1)
    expect(q.peepFront()).toBe(-1)
    console.log(q.front, q.back)
    q.pushFront(2)
    expect(q.peepFront()).toBe(2)
  })
})
