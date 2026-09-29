def create_user(name, age):  
    print(f'User: {name}, Age: {age}')

create_user('Maxmud', 21) #positional arguments
create_user(age=25, name='Timur') #key arguments

def create_profile(name, country='Uzbekistan'): # country is default argument
    print(f'Name: {name}, Country: {country}')

create_profile('Maxmud')
create_profile(country='Kazakhstan', name='Timur')
create_profile('John', 'USA')


def sum_numbers(*args):  #we use args when we dont know how many arguments we have
    print(sum(args))    #we get arguments in tuple
                        #args gets positional arguments
sum_numbers(1,2,3)
sum_numbers(10,20,30,40)


def show_args(*args):
    print(args)
    print(type(args))
    print(len(args))

show_args(10,20,30)

#-------------------------------------------------------

def show_kwargs(**kwargs):  #kwargs gets key arguments
    print(kwargs)           #we get kwargs in dict
    print(type(kwargs))
    print(len(kwargs))

show_kwargs(name='Maxmud', age=21, country='Uzbekistan')


def show_all(name, *args, **kwargs):
    print(f'''
    Name: {name}
    Args: {args}
    Kwargs: {kwargs}
''')

show_all('Maxmud', 10,20,30, age=21, country='Uzbekistan')

#######################################################
#######################################################
#######################################################

def test():
    print('A')
    return 10
    print(B)

def check_number(num):
    if num>0:
        return 'Positive'
    return 'Not Positive'

def check_discount(price, discount=0):
    if discount>0:
        return price-(price*(discount/100))
    return price

print(check_discount(100))
print(check_discount(100, 20))


# SCOPE: LOCAL AND GLOBAL
#-------------- LOCAL inside of function ---------------

# def test():
#     x = 10      #we cant write print(x) out of function
#     print(x)
# test() 

#-------------- GLOBAL out of function --------------

# def test2():
#     print(x)    # we can use out variable inside of function
#                 # but cant use inside variable for out
# x = 77
# test2()
#######################################################

# c = 50 #global

# def test3():
#     c = 100 #local
#     print(c)

# test3()
# print(c)


########################################################

# IF WE WANT TO CHANGE GLOBAL VARIABLE INSIDE OF OUR FUNCTION

# x = 100

# def change():
#     global x
#     x = 200

# change() # if we dont call change() global x equals to 100
# print(x) # 200, because we call change()


#########################################################
#-------------Functions Deep Dive - LEGB ----------------

# L - LOCAL (inside of function)
# E - ENCLOSING (out of function)
# G - GLOBAL (on level of files)
# B - BUILT-IN (built-in functions print, len, sum and etc)
# Local -> Enclosing -> Global -> Built-in

z = 10
def test():
    z = 20 # it finds LOCAL and stops search
    print(z)

x = 10 # global
def test2():
    print(x) # he cant find a local and starts to search out of fucntion

def outer():
    x = 20 #enclosing

    def inner():
        print(x)

    inner()


################ nonlocal #######################

def outer_func():
    x = 10

    def inner_func():
        nonlocal x  #nonlocal changes x of outer function
        x = 20

    inner_func()


def get_user_info(**kwargs):
    return kwargs

print(get_user_info(name='Maxmud', age=21, is_developer=True))


def calculate(a,b,c):
    return a+b+c

numbers = (10,20,30)
print(calculate(*numbers))


######################################################

def create_profile(name, age=0, *skills, **extra):
    if age < 18:
        return 'Acess denied'
    else:
        profile = {
            'name': name,
            'age': age,
            'skills': list(skills),
        }

        return {**profile, **extra}

print(create_profile('Max', 18, 'Python', 'SQL', city='Tashkent'))


######################### CLOSURE #########################

def make_power(n):
    def degree(num):
        return num**n
    return degree

square = make_power(2)
triple = make_power(3)
quadro = make_power(4)

print(square(5))
print(quadro(2))


####################### LAMBDA ##########################

def double(x):
    return x*2

lam_double = lambda x: x*2

print(lam_double(5))


numbers = [1,4,10,8]
res = sorted(numbers, key=lambda x:x**2)
print(res)

res2 = sorted(list(map(lambda x:x**2, numbers)))
print(res2)


##########################################################3

# products = [
#     {"name": "Laptop", "price": 1200, "stock": 5},
#     {"name": "Phone", "price": 800, "stock": 0},
#     {"name": "Monitor", "price": 400, "stock": 10},
#     {"name": "Keyboard", "price": 100, "stock": 20},
#     {"name": "Tablet", "price": 600, "stock": 3}
# ]

# def analyze_products(products, min_price=300):
#     filtered = [{
#         "name": product["name"],
#         "total_value": product["price"]*product["stock"]
#     }
#     for product in products
#     if product["price"]>=min_price and product["stock"] != 0
#     ]

#     return sorted(
#         filtered, key=lambda x:x["total_value"],
#         reverse=True
#     )

# print(analyze_products(products))



employees = [
    {"name": "Ali", "age": 22, "salary": 500, "skills": ["python", "sql"]},
    {"name": "Vali", "age": 17, "salary": 3000, "skills": ["html"]},
    {"name": "Sardor", "age": 28, "salary": 8000, "skills": ["python", "django"]},
    {"name": "Aziz", "age": 31, "salary": 6500, "skills": ["java", "sql"]},
    {"name": "Bek", "age": 25, "salary": 4500, "skills": ["python"]},
]

def analyze_employees(employees, min_age=18, min_salary=4000, **kwargs):
    filtered = [
        {
        "name": employee["name"],
        "salary": employee["salary"],
        "skill_count": len(employee["skills"])}
        for employee in employees
        if employee['age']>=min_age and employee['salary']>=min_salary
    ]    

    return sorted(filtered, key=lambda x:x["salary"], reverse=True)

print(analyze_employees(employees, departmen='IT'))