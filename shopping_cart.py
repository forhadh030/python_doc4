print("""Hello shoppers! Welcome to Syed's Supermarket.
                Rules are very simple:
                1) 'add' to add item to the cart
                1: 'quit' to quit shopping and checkout
                2: 'remove' to remove most recent added product product.
                3: Have fun! :) \n
            """)

class Cart():

    def __init__(self, products):
        self.products = products

    # Method to show ShoppingBag
    def showCart(self):
        print("Checking out all of these products: ")
        for item in self.products:
            print(item, end=", ")
    
    # Method to add to the ShoppingBag
    def addToCart(self):
        product = input("What would you like to add? ")
        self.products.append(product)
        print(self.products)

    # Method to delete item from shopping bag
    def remove_product(self):
        del self.products[-1]
        print(f"This is what you have so far {self.products}")


def run():
    your_cart = Cart([])
    while True:
        response = input("What do you want to do - Add/Remove or Quit? ")
        if response.lower() == 'add':
            your_cart.addToCart()
        if response.lower() == 'remove':
            your_cart.remove_product()
        if response.lower() == 'quit':
            print('Here is your bag...')
            your_cart.showCart()
            break
run()