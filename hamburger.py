# Authors: Isaiah Strong, Adam Ross, Brandon Cragun, Caden Plewe, Gibson Bailey
# Description: This program will track how many hamburgers each driver (customer) delivers

#this will import random number range
import random

#this class will collect orders
class Order:
    #this constructor creates an instance variable for burger_count
    def __init__(self):
        self.burger_count = self.randomBurgers()
    #this method will assign a random value to the number of burgers
    def randomBurgers(self):
        return random.randrange(1,20)
    
#this class will create a list of customer names
class Person():
    def __init__(self):
        self.customer_name = self.randomName()
    def randomName(self):
        asCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms",
                       "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]
        return random.choice(asCustomers)
    
# this class will inherit from the Person class
class Customer(Person):
    def __init__(self):
        super().__init__()
        self.order = Order()

# Initializing a queue able to handle 100 drivers
q = []

    # creates a dictionary to store customer name and amount of burgers ordered
customerDict = {}

for iCount in range (0,100):
    q.append(Customer())

for oCustomer in q:
    if oCustomer.customer_name in customerDict:
        customerDict[oCustomer.customer_name] += oCustomer.order.burger_count
    else:
        customerDict[oCustomer.customer_name] = oCustomer.order.burger_count

listSortedCustomers = sorted(customerDict.items(), key=lambda x: x[1], reverse=True)
orders = ""
for customer in listSortedCustomers: 
    orders += customer[0].ljust(25) + str(customer[1]) + "\n"
print(orders)