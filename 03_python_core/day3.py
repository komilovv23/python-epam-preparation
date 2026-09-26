# users = [
#     {
#         "name": "Ali",
#         "age": 21,
#         "orders": [
#             {"id": 1, "amount": 120},
#             {"id": 2, "amount": 300}
#         ]
#     },
#     {
#         "name": "Vali",
#         "age": 25,
#         "orders": [
#             {"id": 3, "amount": 500},
#             {"id": 4, "amount": 150},
#         ]
#     },
#     {
#         "name": "Sardor",
#         "age": 19,
#         "orders": [
#             {"id": 5, "amount": 50},
#             {"id": 6, "amount": 70},
#         ]
#     }
# ]

# results = []
# for i in users:
#     total = 0
#     for j in i['orders']:
#         total += j['amount']

#     results.append({
#         "name": i["name"],
#         "total": total
#     })

# print(results)
# top_user = max(results, key=lambda x: x['total'])
# print(top_user['name'])
# print([i['name'] for i in results if i['total'] >= 400])
# print(sorted([i['total'] for i in results])[:2])
# print(sorted(res)[:2])


# for i in users:
#     total = 0
#     for j in i['orders']:
#         total += j['amount']
    
#     if total>400:
#         print(f'{i['name']}: {total}')


#----------------------------------------------------

orders = [
    {"users": "Ali", "amount": 120, "status": "paid"},
    {"users": "Vali", "amount": 500, "status": "paid"},
    {"users": "Sardor", "amount": 300, "status": "cancelled"},
    {"users": "Aziz", "amount": 700, "status": "paid"},
    {"users": "Bek", "amount": 150, "status": "cancelled"},
    {"users": "Jasur", "amount": 400, "status": "paid"}                    
]

paid = [i for i in orders if i['status'] == 'paid']
top_2 = sorted(paid, key=lambda x: x['amount'])[2:]
# res = [
#     {"name": i['users'],
#     "amount": i['amount']}
#     for i in top_2
# ]
# print(res)