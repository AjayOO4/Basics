productCost = input("Enter Price of the Product: ")
productCost = int(productCost)
stateTax = 0.08
deliveryPrice = 5.00
loyaltyPoints = 0

if productCost < 500:
    print("Delivery Charges are applicable: " + str(deliveryPrice))
    finalPrice = (productCost + (productCost * stateTax)) + deliveryPrice
else:
    print("You are eligible for Free Shipping and Discounts")
    discount = productCost * 0.05
    finalPrice = ((productCost - discount) + (productCost * stateTax))
    loyaltyPoints = 100

print("The Final price is %f and loyalty points earned %d " % (finalPrice, loyaltyPoints))