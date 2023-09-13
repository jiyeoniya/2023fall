import re

def samechar(S):
    pattern = r'(.)\1+'
    judge = bool(re.search(pattern, S))
    if judge:
        return "Included"
    else:
        return "Not included"


S = input()
print(samechar(S))