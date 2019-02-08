from product import *

# Create an object for each product. Name each object product1, product2, etc.
product1 = Product("Ultrasonic range finder", 2.5, 5)
product2 = Product("Servo Motor", 14.99, 10)

# The following is a list containing each of the 6 product objects created above
products = [product1, product2, product3, product4, product5, product6]

def printStock():
    print()
    print("Available Products")
    print("------------------")
    for i in range(0,len(products)):
       # if the quantity for the product is  > 0:
            print(str(i)+")",products[i].name, "$", products[i].price)
            print()
def main():
    # Modify the previous code to use the objects above and the methods from the Product class
main()
    cash = float(input("How much money do you have? $"))
    while cash > 0:
        printStock()
        vals = input("Enter product ID and quantity you wish to buy: ").split(" ")
        if vals[0] == "quit": break
        prodId = int(vals[0])
        count = int(vals[1]) 

   if products[prodId].checkStock(count):


    
