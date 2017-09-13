class Tree(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        left = None if self.left is None else self.left.data
        right = None if self.right is None else self.right.data
        return '(D:{}, L:{}, R:{})'.format(self.data, left, right)

def build_tree_breadth_first(sequence):
    # Create a list of trees
    forest = [Tree(x) for x in sequence]

    # Fix up the left- and right links
    count = len(forest)
    for index, tree in enumerate(forest):
        left_index = 2 * index + 1
        if left_index < count:
            tree.left = forest[left_index]

        right_index = 2 * index + 2
        if right_index < count:
            tree.right = forest[right_index]
    return (forest)
def main():
    data = [1,5,3,6,4]
    root = build_tree_breadth_first(data)
    print(root)

if __name__ == '__main__':
    main()