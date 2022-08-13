## Given a binary number convert it to hexadecimal.
## Sample Testcase :
## INPUT
## 1100100
## OUTPUT
## 64

b = int(input(),2) # Here the 2 represents in which base
print(hex(b)[2:]) # Here we are excluding the first 2 digits beacause it is not necessary
