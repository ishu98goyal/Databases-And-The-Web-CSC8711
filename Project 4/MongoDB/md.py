# Query 4: Get the names of customers who had to wait the longest for their orders to be shipped.


from datetime import datetime
from dateutil import parser
import pymongo
client = pymongo.MongoClient()
db = client['moDB']

customer_wait_times = {}
longest_wait_customers=[]
for order in db.orders.find():
    customer_no = order['CUSTOMER']
    if 'SHIPPEDDATE' in order:
        shipped_date = parser.parse(order['SHIPPEDDATE'])
    
        received_date = parser.parse(order['RECEIVEDDATE'])

        wait_time = (shipped_date - received_date).days

        if customer_no not in customer_wait_times:
            customer_wait_times[customer_no] = 0

        if wait_time > customer_wait_times[customer_no]:
            customer_wait_times[customer_no] = wait_time

    sorted_customers = sorted(customer_wait_times.items(), key=lambda x: x[1], reverse=True)
    longest_wait_customers = [db.customers.find_one({'CNO': customer[0]})['CNAME'] for customer in sorted_customers[:5]]

print(longest_wait_customers[0])
