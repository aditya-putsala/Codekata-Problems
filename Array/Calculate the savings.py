## A person saves his monthly saving according to given schema. He saves same amount of money which is equal to the money saved in immediate previous two months. Assume, initially he saved 1000 rupees and in first month he saved another 1000. Your task is to tell how much he had totally saved at the end of ‘n’ months

## Input Description:
## You will be given a number ‘n’->No. of months

## Output Description:
## Print the total savings at the end of ‘n’ months

## Sample Input :
## 1
## Sample Output :
## 2000

n = int(input())
l0 = 1000
l1 = 1000
ln = 0
count = 0
sum = 0
a = []
while count<n+1:
    a.append(l0)
    ln = l0 + l1
    l0 = l1
    l1 = ln
    count =count + 1
    
for i in a:
    sum = sum + i
print(sum)
