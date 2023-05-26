### Python Exercises: Variables (3 pts.)
hometown = 'Suryapet'
# Place other variables here
x = 298784
j = 5
l = 10
z = j+l
print(z)
t = q = r = s = 'education'

### Python Exercises: Data Types (2 pts.)
def data_types():
    a = ["apple", "banana", "cherry"]
    print(type(a)) 
    b = ("apple", "banana", "cherry")
    print(type(b)) 
    # Place print statement here
    c = False
    print(type(c)) 
    # Place print statement here
    d = 'covid-19'
    print(type(d)) 
    # Place print statement here
    e = int(487)
    print(type(e)) 

data_types()

### Python Exercises: Data Types 2 (3 pts.)
def data_types2():
    a = ["apple", "banana", "cherry"]
    b = ("apple", "banana", "cherry")
    c = False
    d = 'covid-19'
    e = int(487)
    # Use a single print statement to output data types
    print(" DataType of variable a is - ",type(a) ,"\n", "DataType of variable b is - ",type(b) ,"\n", "DataType of variable c is - ",type(c) ,"\n", "DataType of variable d is - ",type(d) ,"\n", "DataType of variable e is - ",type(e) )

data_types2()

### Python Exercises: Iteration (2 pts.)
def food_loop():
    lunches = ['burger','apple','soba','chahan']
    # for loop goes here
    for x in lunches:
        print(x)
        if x == 'soba': 
            break

food_loop()
