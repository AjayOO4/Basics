TAX = 1.08
moreProducts = True
total = 0

while moreProducts is True:
    productCost = input("Enter the price of the product: ")
    productCost = float(productCost)
    finalPrice = productCost * TAX
    total = total + finalPrice
    answerFlag = input("Do you have More products? [Y/N]")
    if answerFlag == "Y" or answerFlag == "y":
        moreProducts = True
    else:
        moreProducts = False

print("Final Price of all your products: %f" %total)