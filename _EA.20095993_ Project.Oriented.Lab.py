'''
CMPT 120 Intro to Programming
Project-Oriented Lab
Author: Erin Alvarico
Created: November 9th, 2018
'''

# Added class Product to make product objects and store specific information
# about each similar object.

class Product:

    # The information stored in class for object
    # Takes information from productList and uses info to make object
    # via parameters fed.

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)

    # Function within Product class to check if there is enough stock
    # of specific product

    def checkStock(self, quantity):
        if quantity <= self.quantity:
            return True

    # Function within Product class to calculate total price of
    # how much is trying to be bought of a product

    def calculateTotalPrice(self, quantity):
        return quantity * self.price

    # Function within Product class to update the stock
    # amount after purchase.

    def updateQuantity(self, quantity):
        self.quantity = self.quantity - quantity


# The creation of an object for each product given with parameters (name, price, stock)

product1 = Product("Ultrasonic range finder", 2.50, 4)
product2 = Product("Servo motor", 14.99, 10)
product3 = Product("Servo controller", 44.95, 5)
product4 = Product("Microcontroller Board", 34.95, 7)
product5 = Product("Laser range finder", 149.99, 2)
product6 = Product("Lithium polymer battery", 8.99, 8)

# The list of products offered in an array

productList = [ product1, product2, product3, product4, product5, product6 ]

# Functions for main class to call
# Print stock will print the product and the price to the user

def printStock():
    print()
    print("Available Products")
    print("------------------")

    # For loop to loop through every object in productList
    # Range is from object 0 to last object in the list

    for i in range(0, len(productList)):

        # If loop to determine if there is at least one of the product in stock
        # to print the object name and price to be sold: available

        if productList[i].quantity > 0:

            print(str(i)+")", productList[i].name, "$", productList[i].price)
            print()

# Main class is run
# Code starts here

def main():

    # Asks user for input for amount of money they have to spend (float variable)

    cash = float(input("How much money do you have? $"))

    # While loop goes on until user does not have enough money to purchase
    # anymore products or if there is no more products to buy in stock

    while cash > 0:

        # Run printStock() function to print all available products

        printStock()

        # Asking for the user to request the product they wish to purchase
        # Creates vals as an array containing productID (name) and quantity(stock)

        vals = input("Enter product ID and quantity you wish to buy: ").split(" ")

        # if input = "quit" then the program terminates and user no longer can purchase.

        if vals[0] == "quit":
            break

        # Initiating variables where position 0 in array is productID (name) and
        # position 1 in array is count (stock).

        prodId = int(vals[0])
        count = int(vals[1])

        # If loop to determine if the amount of the product desired to be purchased
        # is within the amount of products available.

        if productList[prodId].quantity >= count:

            # If loop to determine if the user has enough money to purchase
            # the amount of product desired.

            if cash >= productList[prodId].price * count:

                # Subtracting amount of desired products purchased from total
                # quantity of product available.

                # Subtracting the amount of money from user's wallet by the amount
                # of products desired to buy.

                productList[prodId].quantity -= count
                cash -= productList[prodId].price * count

                # Print new information to inform user of how much money they
                # have after purchase.

                print("You purchased", count, productList[prodId].name + ".")
                print("You have $", "{0:.2f}".format(cash), "remaining.")

                print("")
                input("[ Press Enter to Continue ]")

                # If not enough money in user's wallet, print message to notify
                # user the purchase is not available because of insufficient
                # funds

            else:
                print("Sorry, you cannot afford that product.")

                print("")
                input("[ Press Enter to Continue ]")

        # If there are not enough of the desired product, print message to notify
        # user the purchase is not available because of insufficient stocks

        else:
            print("Sorry, we are sold out of", productList[prodId].name)

            print("")
            input("[ Press Enter to Continue ]")
main()
