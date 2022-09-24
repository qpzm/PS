from sys import stdin, stdout

tree = dict() # {}

N = int(stdin.readline().strip())
for _ in range(N):
    node, left, right = stdin.readline().strip().split()
    tree[node] = (left, right)

# left tree -> me -> right tree
def inorder(node):
    left, right = tree[node] # node = A left: B, right: C
    if left != '.':
        inorder(tree[node][0])
    stdout.write(node)
    if right != '.':
        inorder(tree[node][1])

# me -> left tree -> right tree
def preorder(node):
    left, right = tree[node]
    stdout.write(node)
    if left != '.':
        preorder(tree[node][0])
    if right != '.':
        preorder(tree[node][1])

def postorder(node):
    left, right = tree[node]
    if left != '.':
        postorder(tree[node][0])
    if right != '.':
        postorder(tree[node][1])
    stdout.write(node)

preorder('A')
print()
inorder('A')
print()
postorder('A')
