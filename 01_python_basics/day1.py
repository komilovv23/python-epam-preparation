name = "Maxmudjon"
age = 21
city = "Tashkent"

print(name)
print(age)
print(city)

price = 120
quantity = 3
overall = price * quantity
print(overall)

age = 21
if age >=18:
    print("Adult")
else:
    print("Minor")

price = 100
quantity = 7

overall = price*quantity
if overall>500:
    print("Discount")
else:
    print("No Discount")


password = 'python123'

age = 21
password = 'python123'

if age >=18 and password == 'python123':
    print('Access granted')
else:
    print('Access denied')


age = 22
password = 'python123'
is_admin = True
is_blocked = True

if not is_blocked:
    print('Access granted')
else:
    print('Access denied')


numbers = [5,12,7,20,13]
for i in numbers:
    if i > 10:
        print(i)

prices = [120,400,80,700,300]
res = [i for i in prices if i >= 300]
print(res)

user = [
    {"name": "Ali", "age": 17},
    {"name": "Vali", "age": 22},
    {"name": "Sardor", "age": 19},
    {"name": "Bobur", "age": 16}
]

for i in user:
    if i['age'] >= 18:
        print(i['name'])

        #or

res2 = [i['name'] for i in user if i['age'] >= 18]
print(res2)