## Find the minimum among 10 numbers.
## Sample Testcase :
## INPUT
## 5 4 3 2 1 7 6 10 8 9
## OUTPUT
## 1

n = list(map(int,input().split()))
sum = 1

for i in n:
    if sum > i:
        sum = i
print(sum)
    
