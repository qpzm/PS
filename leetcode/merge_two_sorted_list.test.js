const list = require('./merge_two_sorted_list');

test('Merge two empty lists', () => {
  let ans = new list.ListNode(1);
  ans.next = new list.ListNode(2);
  let received = list.mergeTwoLists(new list.ListNode(1), new list.ListNode(2))
  expect(received).toStrictEqual(ans);
});
