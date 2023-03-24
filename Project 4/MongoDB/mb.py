# Query 2: Get the names of customers who have ordered parts only from employees living in Wichita.

import pymongo
client = pymongo.MongoClient()
db = client['moDB']

res = []
for c in db.customers.find({}, {'CNO': 1, '_id': 0, 'CNAME': 1}):
    for e in db.employees.find({'CITY': 'Wichita'}, {'ENO': 1, '_id': 0}):
        if db.orders.count_documents({'CUSTOMER': c['CNO'], 'TAKENBY': e['ENO']}) > 0:
            res.append(c['CNAME'])

for i in res:
    print(i)
