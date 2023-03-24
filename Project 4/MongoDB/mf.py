# Query 6: Get the names of employees who have never made a sale to a customer in the same zipcode as themselves.

import pymongo
client = pymongo.MongoClient()
db = client['moDB']
employees = db.employees.find()
result = []
for employee in employees:
    orders = db.orders.find({'TAKENBY': employee['ENO']})
    customer_zips = set()
    for order in orders:
        customer = db.customers.find_one({'CNO': order['CUSTOMER']})
        if customer is not None:
            customer_zips.add(customer['ZIP'])
    if employee['ZIP'] not in customer_zips:
        result.append(employee['ENAME'])
for r in result:
    print(r)
    