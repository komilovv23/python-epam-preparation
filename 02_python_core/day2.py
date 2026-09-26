# numbers = [4,7,12,19,20,25,30]
# count = 0
# for i in numbers:
#     if i % 2 == 0:
#         count += 1

# print(count)

# orders = [120,450,80,700,150,30,900,200]
# count = 0
# for i in orders:
#     if i < 100:
#         continue
#     elif i == 900:
#         break
#     else:
#         print(f'Order: {i}')

# correct_password = '112233'
# attempts = 3

# while attempts > 0:
    # password = input('password: ')
    # if password == correct_password:
    #     print('acess')
    #     break
    # else:
    #     attempts -=1
    #     print(f'wrong password, you have {attempts} attempts')
    #     if attempts == 0:
    #         print('wrong password, try again after 24 hours')

# orders = [120, -1, 450, 80, 700, 0, 159, 999, 300]
# amount = 0
# while amount < 5:
    # for i in range(len(orders)):
    #     if amount < 5 and orders[i] > 0:
    #         print(orders[i])  
    #         amount+=1  
    #     elif orders[i] == 999:
    #         break
    #     else:
    #         continue
    # print(f'Processed: {amount}')


# def square(number):
#     res = number**2
#     return res

# print(square(120))

# def calculate(num1, num2):
#     res = (num1+num2)*2
#     return res

# print(calculate(3,4))

# def test(x):
#     if x > 10:
#         return 'Big'

#     return 'Small'

# print(test(15))
# print(test(5))


orders = [
    {"id": 1, "amount": 120, "status": "paid"},
    {"id": 2, "amount": 50, "status": "cancelled"},
    {"id": 3, "amount": 450, "status": "paid"},
    {"id": 4, "amount": -20, "status": "paid"},
    {"id": 5, "amount": 700, "status": "paid"},
    {"id": 6, "amount": 80, "status": "paid"},
    {"id": 7, "amount": 999, "status": "paid"},
    {"id": 8, "amount": 300, "status": "paid"},
]

def is_big_order(amount):
    for i in orders:
        if amount >=400:
            return True
        return False

obr = []
for i in orders:
    if i['status'] == 'cancelled' or i['amount'] == 0:
        continue
    elif i['amount'] == 999:
        break
    else:
        obr.append(i)

for i in obr:
    id = i['id']
    amount = i['amount']
    is_big = is_big_order(i['amount'])

    print(f'id:{id}, amount: {amount}, is big order: {is_big}')


text = "Python EPAM Internship"
print(len(text))
print(text.upper())
print(text.lower())
print('Python' in text)
print(text.replace('Python', 'Java'))
print(text.split()[0])
print([i for i in text])

print(text.split())
print(len(text.split()))
print(max(text.split(), key=len))  #search the longest word in text
print([i for i in text.split() if len(i)>5]) #words that length more than 5
a = text.split()[::-1]  #reverse list
print(' '.join(a)) #make from elements of list to text

users = [
    {"name": "Ali", "age": 17, "city": "Tashkent", "active": True},
    {"name": "Vali", "age": 27, "city": "Samarkand", "active": True},
    {"name": "Sardor", "age": 19, "city": "Tashkent", "active": False},
    {"name": "Aziz", "age": 25, "city": "Bukhara", "active": True},
    {"name": "Bek", "age": 16, "city": "Tashkent", "active": True},
    {"name": "Jasur", "age": 30, "city": "Tashkent", "active": True},
]

def is_adult(age):
    if age >= 18:
        return True
    return False

for i in users:
    print(is_adult(i['age']))

for i in users:
    name = i['name']
    city = i['city']
    adult = is_adult(i['age'])
    if is_adult(i['age']) == False or i['active'] == False:
            continue
    else:
        print(f'Name: {name} | City: {city} | Adult: {adult}')

res = [i for i in users if is_adult(i['age'])==True and i['city']=='Tashkent' and i['active'] == True]
print(len(res))

res2 = [i['age'] for i in users if is_adult(i['age'])==True and i['active'] == True]
print(sum(res2)/len(res2))

