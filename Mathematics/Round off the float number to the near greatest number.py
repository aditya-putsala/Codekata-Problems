## Given a floating point number with 1 decimal place round it off to nearest greater integer and print it.
## Sample Testcase :
## INPUT
## 2.6
## OUTPUT
## 3

n = input()
print(int(n[:len(n)-2])+1)
