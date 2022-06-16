colors = ["red", "green", "blue", "yellow", "violet", "orange", "indigo"]
#extend method is used to add two arrays together
#For example

moreColors = ["Navy", "Brown"]
colors.extend(moreColors)
print("Extended array : ", colors)
print(colors[3])

print(len(colors))

colors.append("black")
print(len(colors), colors)

for eachColor in colors:
    print("Before Pop", eachColor)

colors.pop()
for eachColor in colors:
    print("After pop", eachColor)

colors.pop(2)
print("After popping index 2 : ", colors)
cart = [123, 568, 9088, 1022]
total = 0
for allSale in cart:
    total = total + allSale
print("All sales bill: " + str(total))