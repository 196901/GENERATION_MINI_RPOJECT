order_list = [{
                "customer_name" : "Mike",
                "customer_address" : "16 London Road, London, E10 2HR",
                "customer_phone" : "078957253617",
                "courier" : "John",
                "status" : "preparing"},
                {
                "customer_name" : "David",
                "customer_address" : "345 Old Street, London, SE5 8AT",
                "customer_phone" : "078957253617",
                "courier" : "Claire",
                "status" : "preparing"},
                {
                "customer_name" : "Arben",
                "customer_address" : "28 Old Kent Road, London, SE1 5TY",
                "customer_phone" : "078957253617",
                "courier" : "Micheal",
                "status" : "preparing"}
]
for order in order_list:
    print(order)
for index, item in enumerate(order_list):
    print(index, item)