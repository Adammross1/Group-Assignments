# Authors: Isaiah Strong, Adam Ross, Brandon Cragun, Caden Plewe, Gibson Bailey
# Description: This program will track how many hamburgers each driver (customer) delivers

#this will import random number range
import random
from queue import Queue

#this class will collect orders
class Order:
    #this constructor creates an instance variable for burger_count
    def __init__(self, burger_count):
        self.burger_count = burger_count
        burger_count = self.randomBurgers()
    #this method will assign a random value to the number of burgers
    def randomBurgers(self):
        return random.randrange(1,20)
    
#this class will create a list of customer names
class Person(Order):
    def __init__(self, burger_count,customer_name):
        super().__init__(burger_count)
        self.customer_name = customer_name
        customer_name = self.randomName()
    def randomName(self):
        asCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms",
                       "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]
        return random.choice(asCustomers)
    
# this class will inherit from the Person class
class Customer(Person):
    def __init__(self, customer_name,burger_count, order):
        super().__init__(customer_name,burger_count)
        self.order = order
        order = burger_count

# Initializing a queue able to handle 100 drivers
q = Queue(maxsize = 100)

# creates a dictionary to store customer name and amount of burgers ordered
customerDict = {
  Person.customer_name:Order.burger_count
}

#this variable will pass values into the Order class
order1 = Order(0)
print(Order.randomBurgers(order1))