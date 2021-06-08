num1 = 42 #variable declaration add value
num2 = 2.3 #variable declaration add value
boolean = True #variable declaration
string = 'Hello World' #initialize strings. variable declaration
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']#variable declaration,initialize list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration,initialize dictionary 
fruit = ('blueberry', 'strawberry', 'banana')#variable declaration, tuples
print(type(fruit))#access value tuples
print(pizza_toppings[1])#acess value list
pizza_toppings.append('Mushrooms')#list access value
print(person['name'])#access dictionary value
person['name'] = 'George' #change value dictionary
person['eye_color'] = 'blue' #change value dictioary
print(fruit[2]) #tuples access value

if num1 > 45: #conditional if ,stop
    print("It's greater")
else:#conditional else
    print("It's lower")

if len(string) < 5: #conditional if lenght check
    print("It's a short word!")
elif len(string) > 15: #conditional else if lenght check
    print("It's a long word!")
else: #conditional else
    print("Just right!")

for x in range(5): #for loop
    print(x)
for x in range(2,5):
    print(x)#for loop sequence
for x in range(2,10,3): #for loop sequence
    print(x)
x = 0 #variable declaration
while(x < 5): #while loop
    print(x)
    x += 1 

pizza_toppings.pop()#AttributeError: 'tuple' object has no attribute 'pop'
pizza_toppings.pop(1)#

print(person)
person.pop('eye_color')#AttributeError: 'tuple' object has no attribute 'pop'
print(person)

for topping in pizza_toppings:#for loop start
    if topping == 'Pepperoni':#if conditional 
        continue
    print('After 1st if statement')
    if topping == 'Olives':#if conditional 
        break #for loop break

def print_hello_ten_times():#function 
    for num in range(10):#for loop 
        print('Hello')

print_hello_ten_times() #function

def print_hello_x_times(x):#function
    for num in range(x):#for loop
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10): #function 
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()#function return
print_hello_x_or_ten_times(4)#function return


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)