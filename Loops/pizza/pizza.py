#Codigo por Roberto Ochoa Cuevas

# ask for how much money they want to spend
print("-> Pizza Robert <- ")
money = int(input('how many money you want to spend? '))

# create arrays we are going to need
addedToppings = []
toppings = ['pepperoni ($1)',"Salami ($1)","chesse ($2)"]
pizzas = ['small ($10)','medium ($13)', 'large ($16)']
bill = 0

# ask what type of pizza they want
print(f"Available pizzas: {pizzas}")
pickedPizza = input('pick a pizza pls ').lower()

if pickedPizza == 'small':
    bill += 10
elif pickedPizza == 'medium':
    bill += 13
else:
    bill += 16

# show how much they have spend
print(toppings)
if input(f"actual bill: {bill}, you want to add toppings? yes/no ").lower() == 'yes':
    
    #Loop for toppings
    while True:
        toppings = input(f'pick a topping or write "pay" to pay , your bill is {bill} ').lower()
        
        if bill >= money:
            print('you have no more money available')
            break

        if toppings == 'pay':
            break
        elif toppings == 'pepperoni' or toppings == 'salami':
            bill+=1
        elif toppings == 'chesse':
            bill+=2

# pay time 
print(f"time to pay :), your bill is {bill}")
