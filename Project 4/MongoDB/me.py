# Query 5: Get the names of parts that have been ordered the most in terms of quantity.

import pymongo
client = pymongo.MongoClient()
db = client['moDB']

orders = db.orders.find()
part_counts = {}
for order in orders:
    for item in order['ITEMS']:
        part_no = item['PARTNUMBER']
        if part_no not in part_counts:
            part_counts[part_no] = 0
        part_counts[part_no] += item['QUANTITY']
parts = db.parts.find({'PNO': {'$in': list(part_counts.keys())}})
result = []
for part in parts:
    part_no = part['PNO']
    part_count = part_counts[part_no]
    result.append((part['PNAME'], part_count))
result.sort(key=lambda x: x[1], reverse=True)
for r in result[:2]:
    print(r[0])
    
