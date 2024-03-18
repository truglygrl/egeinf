f = open('24_4__1kaco.txt')
s = f.readline()
def max_len_substring(s: str) -> int:
    if len(s) < 2:
        return len(s)
    left = 0
    right = 1
    max_len = 0
    while right < len(s):
        if s[right] != s[right - 1]:
            max_len = max(max_len, right - left)
        else:
            left = right
        right += 1
    return max(max_len, right - left)
print(max_len_substring(s))