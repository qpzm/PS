const stringShift = require('./perform_string_shifts.js').default
const shifter = require('./perform_string_shifts.js')

describe('shiftLeft', () => {
  test('n = 1', () => {
    expect(shifter.shiftLeft("abc", 1)).toStrictEqual("bca");
  });

  test('n = str.length()', () => {
    expect(shifter.shiftLeft("abc", 3)).toStrictEqual("abc");
  });
});

describe('shiftRight', () => {
  test('n = 1', () => {
    expect(shifter.shiftRight("abc", 1)).toStrictEqual("cab");
  });

  test('n = str.length()', () => {
    expect(shifter.shiftRight("abc", 3)).toStrictEqual("abc");
  });
});

describe('stringShift', () => {
  test('Shift example', () => {
    expect(stringShift("abc", [[0,1],[1,2]])).toStrictEqual("cab");
  });

  test('Shift example', () => {
    expect(stringShift("abcdefg", [[1,1],[1,1],[0,2],[1,3]])).toStrictEqual("efgabcd");
  });
});
