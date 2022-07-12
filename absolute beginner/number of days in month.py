## You will be provided with a number. Print the number of days in the month corresponding to that number.

## Note: In case the input is February, print 28 days. If the Input is not in valid range print "Error".

## Input Description:
## The input is in the form of a number.

## Output Description:
## Find the days in the month corresponding to the input number. Print Error if the input is not in a valid range.

## Sample Input :
## 8
## Sample Output :
## 31

month = [31,28,31,30,31,30,31,31,30,31,30,31]
n = int(input())
if(n>1 and n<13):
    print(month[n-1])
else:
    print("Error")
