productCost = input("Enter Price of the Product: ")
productCost = int(productCost)
stateTax = 0.08
deliveryPrice = 5.00

if productCost < 100:
    print("Delivery Charges are applicable: " + str(deliveryPrice))
    finalPrice = (productCost + (productCost * stateTax)) + deliveryPrice
else:
    print("You are eligible for Free Shipping")
    finalPrice = productCost + (productCost * stateTax)

print("Your final Price is: %f" %finalPrice)