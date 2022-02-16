def addSale():
    product = input("Product")
    price = float(input("Price"))
    sale = (product, price)
    with open('sales.txt', 'a') as sales:
        #product = input('Product:\n')
        #price = input('Price:\n')
        sales.write('\n')
        sales.write(str(sale))
    

def show():
    with open('sales.txt', 'r') as sales:
        for sale in sales:
            if type(int()):
                print(sale)


addSale()

show()