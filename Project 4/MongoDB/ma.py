# Query 1: For each customer, find a list of Order Numbers they have placed.

import pymongo
client = pymongo.MongoClient()
db = client['moDB']

customers = db.customers.find()
result = {}
for customer in customers:
    customer_id = customer['CNO']
    orders = db.orders.find({'CUSTOMER': customer_id})
    orderno = [order['ONO'] for order in orders]
    result[customer_id] = orderno

for cno, orderno in result.items():
    print(f"Customer {cno}: Orders {orderno}")