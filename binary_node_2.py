class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = '*'
        self.right = '*'
    def __str__(self):


from collections import deque

data = [3,5,2,1,4,6,7,8,9,10,11,12,13,14]
n = iter(data)
tree = Node(next(n))
fringe = deque([tree])
while True:
    head = fringe.popleft()
    try:
        head.left = Node(next(n))
        fringe.append(head.left)
        head.right = Node(next(n))
        fringe.append(head.right)
    except StopIteration:
        break

print(tree)
Node()