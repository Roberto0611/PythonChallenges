# Exercise 6: Count the total number of digits in a number
# Write a program to count the total number of digits in a number using a while loop.
# For example, the number is 75869, so the output should be 5.

number = int(input("write a big number: "))
num_digits = 0

while True:
    number = number // 10
    num_digits += 1
    if number == 0:
        break
print(num_digits)

