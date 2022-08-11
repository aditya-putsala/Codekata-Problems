## Rajat is given some special task to calculate the largest sum of two consecutive elements.He solved some of questions but he is not sure whether his answer is correct or not. Your task is to help him in determining whether answers posted by him are correct or not.

## Input Description:
## The first line of the input is a integer N. The second line of the input consists of N space separated integer.

## Output Description:
## Print the max sum of two consecutive numbers from the given N numbers

## Sample Input :
## 5
## 1 5 6 8 3
## Sample Output :
## 14

n = int(input())
k = list(map(int,input().split()))
max_num1 = 0
max_num2 = 0
for i in range(n):
    if max_num1 < k[i]:
        max_num1 = k[i]
k.remove(max_num1)
for i in range(n-1):
    if max_num2 < k[i]:
        max_num2 = k[i]
print(max_num1 + max_num2)
