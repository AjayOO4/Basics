def calDelivery(price):
    if price <= 100:
        cost = 10
    else:
        cost = 0
    return cost

def calTax(saleTax, prodPrice):
    afterTax = prodPrice * saleTax
    return afterTax


tax = 1.08
productCost = input("Enter the price of product: ")
productCost = int(productCost)
deliveryCost = calDelivery(productCost)
taxCost = calTax(tax, productCost)
totalPrice = deliveryCost + taxCost
print("Total Price of the Product: %.2f" %totalPrice)