class Tree:
    def __init__(self, prefix, sub = None):
        if sub is None:
            sub = []
        self.prefix = prefix
        self.subtrees = sub

    def string(self, tab) -> str:
        if len(self.subtrees) == 0:
            return f"'{self.prefix}'"
        s = ""
        for i, tree in enumerate(self.subtrees):

            s += '\n' + ' '*tab + tree.string(tab+len(self.prefix)+6) + " "
        return f"'{self.prefix}' -> {s}"

    def __str__(self):
        return self.string(6)


def group_by_prefix(words: [Tree], start: int, prefix: str) -> (str, [Tree]):
    dic = {}
    letter = ''
    while len(dic) < 2:
        if len(dic) != 0:
            start += 1
            prefix += letter
        dic = {}
        for word in words:
            value = word.prefix
            if len(value) == start:
                dic[''] = [word]
                continue
            letter = value[start]
            if letter in dic:
                dic[letter].append(word)
            else:
                dic[letter] = [word]
    return prefix, [Tree(prefix + letter, dic[letter]) for letter in dic]


all_words = ['deer', 'deals', 'dealsk', 'deal', 'door', 'dog', 'dodge', 'dodatkowe', 'dogs']

root = Tree('')


def add(tree: Tree, s: str, start):
    tree.subtrees.append(Tree(s))
    prefix, grouped = group_by_prefix(tree.subtrees, start, tree.prefix)
    for group in grouped:
        for subtree in group.subtrees:
            if subtree.prefix == group.prefix:
                group.subtrees.remove(subtree)
                group.subtrees += subtree.subtrees
    if tree.prefix == '':
        tree.subtrees = [Tree(prefix, grouped)]
        return tree
    return Tree(prefix, grouped)


root.subtrees.append(Tree('dear'))

root = add(root, 'deels', 0)

print(root)

root.subtrees[0].subtrees[1] = add(root.subtrees[0].subtrees[1], 'deels', 2)

# adding 'deer' and 'deals'

# tree = root.subtrees[0].subtrees[1]
# tree.subtrees.append(Tree('dear'))
# prefix, grouped = group_by_prefix(tree.subtrees, 3, tree.prefix)
# for group in grouped:
#     print(group)
# for group in grouped:
#     print('before')
#     print(group)
#     for subtree in group.subtrees:
#         if subtree.prefix == group.prefix:
#             group.subtrees.remove(subtree)
#             group.subtrees += subtree.subtrees
#     print('after')
#     print(group)
# root.subtrees[0].subtrees[1] = Tree(prefix, grouped)


# add(root, 'deals', 0)
# add(root.subtrees[0], 'dear', 2)
# add(root, 'dear')
# root.subtrees.append(Tree('deals'))
#
# prefix, grouped = group_by_prefix(root.subtrees, 0, '')
#
# print("elements have same prefix: " + prefix)
# root.subtrees.clear()
#
# for group in grouped:
#     print(group)
#
# root.subtrees = [Tree(prefix, grouped)]

sub = None
# instead of this we are finding the biggest prefix of all elements on this level and


# sub = Tree('de')
#
# root.subtrees.append(sub)
#
# sub.subtrees.append(Tree('deer'))
# sub.subtrees.append(Tree('dear'))


print(root)
#
# '' -> 'd'
#     - 'k' -> 'kit'
#            - 'kat'
#     - 'h' -> 'get'
#            - 'give'
