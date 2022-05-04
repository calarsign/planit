'''Get the nth number in the fibonacci sequence given n'''

ctr = 0
n1 = 0
n2 = 1
sum = 0
x = 0
# x stores the value of the fibonacci number

# input number to check fibonacci sequence
n = int(input("Enter a positive integer to find Fibonacci sequence: "))
print("You inputted number ", n)
if n < 0:
    print("Invalid Input!")
elif n == 0:
    x = 0
elif n == 1:
    x = 1
elif n > 1:
    while ctr < n:
        sum = n1 + n2
        n1 = n2
        n2 = sum
        ctr += 1
    x = n1
# this if statement prints the fibonacci sequence
if n >= 0:
    print("Fibonacci number in sequence", n, "is: ", x)








