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


def group_by_prefix(words: [Tree], start: int, prefix: str) -> (int, [Tree]):
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
    id = 0
    for i, letter in enumerate(dic):
        if words[-1] in dic[letter]:
            dic[letter].remove(words[-1])
            id = i
            break
    return id, [Tree(prefix + letter, dic[letter]) for letter in dic]


def add_item_to_tree(tree: Tree, s: str):
    print("add '" + s + "'")
    if len(tree.subtrees) == 0:
        if tree.prefix == s: return
        tree.subtrees = [Tree(s)]
        return
    for child in tree.subtrees:
        if s.startswith(child.prefix):
            print(f"yeah '{s}' starts with '{child.prefix}' so reqursive")
            add_item_to_tree(child, s)
            return
    print("there is a problem, no matches... ://")
    tree.subtrees.append(Tree(s))
    id, grouped = group_by_prefix(tree.subtrees, len(tree.prefix), tree.prefix)
    tree.subtrees = grouped
    add_item_to_tree(tree.subtrees[id], s)
    print(tree)


all_words = ['deer', 'deals', 'dealsk', 'deal', 'door', 'dog', 'dodge', 'dodatkowe', 'dogs']

root = Tree('')
add_item_to_tree(root, 'dear')
print(root)
add_item_to_tree(root, 'deels')
# add_item_to_tree(root, 'deer')
# add_item_to_tree(root, 'deapth')
# add_item_to_tree(root, 'deafinition')
# add_item_to_tree(root, 'deers')
# add_item_to_tree(root, 'dears')
# for x in ['formulate',
# 'feeling',
# 'federation',
# 'formula',
# 'finance',
# 'fox',
# 'forum',
# 'formation',
# 'front',
# 'fast',
# 'frozen',
# 'fuel',
# 'fuss',
# 'fee',
# 'foundation',
# 'disposition',
# 'depart',
# 'debut',
# 'divide',
# 'drawing',
# 'detective',
# 'dozen',
# 'disgrace',
# 'distant',
# 'doctor',
# 'deal',
# 'define',
# 'discreet',
# 'depression',
# ]:
#     add_item_to_tree(root, x)
# add_item_to_tree(root, 'door')
# add_item_to_tree(root, 'fridge')

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

#
# '' -> 'd'
#     - 'k' -> 'kit'
#            - 'kat'
#     - 'h' -> 'get'
#            - 'give'
