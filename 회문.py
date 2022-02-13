import sys
input = sys.stdin.readline

# abcba
# abba

def isitpalindrome(s):
    if len(s) <= 1: return 1
    mid = len(s) // 2
    
    if len(s) % 2: left_word, right_word = s[:mid+1], s[mid:][::-1]
    else: left_word, right_word = s[:mid], s[mid:][::-1]
    return left_word == right_word

def palindrome(s):
    if len(s) <= 1: return 0
    mid = len(s) // 2
    
    if len(s) % 2: left_word, right_word = s[:mid+1], s[mid:][::-1]
    else: left_word, right_word = s[:mid], s[mid:][::-1]

    for i in range(mid):
        if left_word[i] != right_word[i]:
            new_right_word = []
            for j in range(len(right_word)):
                if j != i: new_right_word.append(right_word[j])

            # if len(s) % 2 and isitpalindrome(s[:mid+1] + new_right_word[::-1]): return 1
            if isitpalindrome(s[:mid] + new_right_word[::-1]): return 1

            new_left_word = []
            for j in range(len(left_word)):
                if j != i: new_left_word.append(left_word[j])

            if isitpalindrome(new_left_word + right_word[::-1]): return 1

            return 2

    return 0


T = int(input())
words = [list(input())[:-1] for _ in range(T)]

for word in words:
    print(palindrome(word))