# Query 3: Get employee numbers and total sales for each employee.

import pymongo
client = pymongo.MongoClient()
db = client['moDB']

orders = db.orders.find()
result = {}
for order in orders:
        taken_by = order['TAKENBY']
        if taken_by not in result:
            result[taken_by] = 0
        for item in order['ITEMS']:
            part = db.parts.find_one({'PNO': item['PARTNUMBER']})
            result[taken_by] += item['QUANTITY'] * part['PRICE']
        
print("Employee : Sales")
for eno, sales in result.items():
    print(f"{eno}     : {sales}")
