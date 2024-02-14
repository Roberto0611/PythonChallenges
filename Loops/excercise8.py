# Exercise 8: Print list in reverse order using a loop
# Given: list1 = [10, 20, 30, 40, 50]

list1 = [10, 20, 30, 40, 50]
x = len(list1) - 1

for i in range(x,-1,-1):
    print(list1[i])
