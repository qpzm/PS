from sys import stdin, stdout, setrecursionlimit
setrecursionlimit(10**8)

def preorder(in_begin, post_begin, length):
    if length == 0:
        return
    root = postorder[post_begin + length - 1]
    i = inorder.index(root, in_begin, in_begin + length)

    left_len = i - in_begin
    right_len = length - 1 - left_len
    stdout.write(f'{root} ')
    preorder(in_begin, post_begin, left_len)
    preorder(i+1, post_begin + left_len, right_len)

if __name__ == "__main__":
    N = int(stdin.readline().rstrip())
    inorder = list(map(int, stdin.readline().rstrip().split()))
    postorder = list(map(int, stdin.readline().rstrip().split()))
    preorder(0, 0, len(inorder))
