from sys import stdin, stdout

def preorder(inorder, postorder):
    if len(postorder) == 0:
        return
    root = postorder[-1]
    i = inorder.index(root)
    left_len, right_len = i, len(inorder) - 1 - i
    in_left, in_right = inorder[:i], inorder[i+1:]
    post_left, post_right = postorder[:left_len], postorder[left_len:left_len + right_len]
    stdout.write(f'{root} ')
    preorder(in_left, post_left)
    preorder(in_right, post_right)

if __name__ == "__main__":
    N = int(stdin.readline().rstrip())
    inorder = list(map(int, stdin.readline().rstrip().split()))
    postorder = list(map(int, stdin.readline().rstrip().split()))
    preorder(inorder, postorder)
