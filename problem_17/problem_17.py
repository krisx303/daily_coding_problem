"""
dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext
"""


def read_word(path: str, start: int) -> (int, int, bool):
    index = start
    length = 0
    level = 0
    if path[start] == '\n':
        level += 1
        index += 1
    while path[index] == '\t':
        level += 1
        index += 1
    contains_dot = False
    while index < len(path) and path[index] != '\n':
        if path[index] == '.':
            contains_dot = True
        length += 1
        index += 1
    return level, length, contains_dot


if __name__ == "__main__":
    path = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"

    stack = []

    max_len = 0
    act_len = 0

    start = 0
    while start < len(path):
        level, length, is_file = read_word(path, start)
        print(level, length, is_file)
        start += level + length
        act_level = max(0, level-1)
        if not is_file:
            while len(stack) > act_level:
                act_len = act_len - stack.pop() - 1
            act_len += length + 1
            stack.append(length)
        else:
            if act_len + length > max_len:
                max_len = act_len + length

    print(max_len)




