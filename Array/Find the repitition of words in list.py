## Given a sentence and string S, find how many times S occurs in the given sentence.If S is not found in the sentence print -1
## Input Size : |sentence| <= 1000000(complexity O(n)).
## Sample Testcase :
## INPUT
## I enjoy doing codekata
## codekata
## OUTPUT
## 1

n = list(input().split())
k = input()
count = 0
for i in n:
    if k == i:
        count = count + 1
if count == 0:
    print(-1)
else:
    print(count)
