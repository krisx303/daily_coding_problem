class Tree:
    def __init__(self, value, sub=None):
        if sub is None:
            sub = []
        self.value = value
        self.length = len(value)
        self.subtrees = sub

    def __str__(self) -> str:
        if len(self.subtrees) == 0:
            return f"'{self.value}'"
        s = ""
        for tree in self.subtrees:
            s += str(tree) + " "
        return f"'{self.value}' -> [{s}]"

    def add_element(self, word):
        self.subtrees.append(Tree(word))
        # reapir tree
        grouped = group_by_prefix(self.subtrees, self.length, self.value)
        print(grouped)
        self.subtrees = [Tree(group[1][0].value) if len(group[1]) == 1 else Tree(group[0], group[1]) for group in
                         grouped]


all_words = ['deer', 'deals', 'dealsk', 'deal', 'door', 'dog', 'dodge', 'dodatkowe', 'dogs']


def group_by_prefix(words: [Tree], start: int, prefix: str) -> [(str, [Tree])]:
    if len(words) == 1:
        return [(words[0].value, [words[0]])]
    # dic = {}
    # for word in words:
    #     word = word.value
    #     if len(word) == start:
    #         dic[''] = [word]
    #         continue
    #     letter = word[start]
    #     if letter in dic:
    #         dic[letter].append(word)
    #     else:
    #         dic[letter] = [word]
    dic = {}
    letter = ''
    while len(dic) < 2:
        if len(dic) != 0:
            start += 1
            prefix += letter
        dic = {}
        for word in words:
            value = word.value
            if len(value) == start:
                dic[''] = [word]
                continue
            letter = value[start]
            if letter in dic:
                dic[letter].append(word)
            else:
                dic[letter] = [word]
    return [(prefix, dic[letter]) for letter in dic]


# def get_longest_prefix(words: [(str, int)], start: int) -> str:
#     size = start
#     letter = None
#     while True:
#         for word, length in words:
#             if letter is None:
#                 if length <= size:
#                     return ''
#                 else:
#                     letter = word[size]
#                     continue
#             if word[size] != letter:
#                 return word[start:size]
#         size += 1


# def group_by_prefix(words: [str], start: int, prefix: str) -> [(str, [str])]:
#     dic = {}
#     for word in words:
#         if len(word) == start:
#             dic[''] = [word]
#             continue
#         letter = word[start]
#         if letter in dic:
#             dic[letter].append(word)
#         else:
#             dic[letter] = [word]
#     return [(prefix + letter, dic[letter]) for letter in dic]


# def create_tree(grouped: [(str, [str])], start: int) -> Tree:
#     for prefix, group in grouped:
#         print(prefix, group)
#         if len(group) == 1:
#             continue
#         g = group_by_prefix(group, start + 1, prefix)
#         create_tree(g, start+1)


# ['deal', 'deals', 'dealsk', 'deer', 'dodatkowe', 'dodge', 'dog', 'dogs', 'door']

# deal -> put d, de, dea, deal on stack
# deals -> is bigger then

root = Tree('')
root.add_element(all_words[0])
print(root)
root.add_element(all_words[1])
print(root)

