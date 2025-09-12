class Product:
    def __init__(self, product_id, product_nm, price, stock):
        self.product_id = product_id
        self.product_nm = product_nm
        self.price = price
        self.stock = stock

    def getStock(self):
        return self.stock
    
    def setStock(self, stock_val):
        if self.stock - stock_val >= 0:
            self.stock -= stock_val
            print(f"Purchased {stock_val} quantity Successfully")
        else:
            print(f"Purchased Failed! The ask quantity {stock_val} is more than the remaining Stock {self.stock}")

class Customer:
    def __init__(self, cust_id, name):
        self.cust_id = cust_id
        self.name = name

    def showInfo(self):
        print(f"Name: {self.name}. Customer ID: {self.cust_id}")

    def buyProduct(self, product_obj):
        if product_obj.getStock() > 0:
            print(f"The remaining Stock of {product_obj.product_nm} is {product_obj.getStock()}")
            quantity = int(input("Enter the Quantity: "))
            product_obj.setStock(quantity)
        else:
            print(f"There is No Stock of {product_obj.product_nm}")

p1 = Product(101, "Lassi", 20, 2)

c1 = Customer(56, 'Amanjyot')
c2 = Customer(52, 'Hrishikesh')
c2.buyProduct(p1)
c1.buyProduct(p1)
c1.showInfo()
print(p1.getStock())