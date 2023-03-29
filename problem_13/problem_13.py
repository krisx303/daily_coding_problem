string = "abcba"
k = 2

# string = "asaagdfhjkbbbababaadsfhgjjashkdlbababasfdfdasdqwe"


def f(s: str, k: int) -> str:
    l_longest = 0
    w_longest = ""
    curr_set = {}
    start_word = 0
    start_search = 0
    end = 0
    while end < len(s)-1:
        for i, letter in enumerate(s[start_search:]):
            if len(curr_set) < k:
                curr_set[letter] = start_search + i
                continue
            elif len(curr_set) == k and letter in curr_set:
                curr_set[letter] = start_search + i
                continue
            else:
                end = start_search + i
                break

        #print(start_word, end)
        #print(curr_set)
        word = s[start_word:end]
        if len(word) > l_longest:
            l_longest = len(word)
            w_longest = word
        # print(s[start_word:end])

        to_rm = min(curr_set, key=lambda x: curr_set[x])
        start_word = curr_set[to_rm] + 1
        curr_set.pop(to_rm)
        #print(f"we need to remove '{to_rm}' with last position at {start_word}")
        #print(f"start new search from {end}")

        start_search = end
    return w_longest

print(f(string, k))

