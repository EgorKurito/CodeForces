#Ходьба по диогонали
n = int(input())
s = list(input())
i = 1
while i < len(s):
    if s[i] + s[i-1] == 'RU':
        n -= 1
        s[i] = 'D'
    elif s[i] + s[i-1] == 'UR':
        n -= 1
        s[i] = 'D'
    i += 1

print(n)
