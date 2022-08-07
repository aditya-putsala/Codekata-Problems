## Given a string S consisting of 2 words reverse the order of two words .
## Input Size : |S| <= 10000000
## Sample Testcase :
## INPUT
## hello world
## OUTPUT
## world hello

s = list(input().split())
k = []
k.append(s[1])
k.append(s[0])
print(" ".join(k))
