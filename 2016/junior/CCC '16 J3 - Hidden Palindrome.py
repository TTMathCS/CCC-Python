def is_palindrome(s):
    return s == s[::-1]


max_len = 0
s = input()
for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        if is_palindrome(s[i:j]):
            max_len = max(max_len, j - i)
print(max_len)
