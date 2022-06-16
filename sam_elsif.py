experience_yr = input("Enter your years of Experience:")
experience_yr = float(experience_yr)

if(experience_yr <= 2.0):
    print("Your designation is Junior Programmer")
elif(experience_yr <= 6.0):
    print("Your designation is Intermediate Programmer")
else:
    print("Your designation is Senior Programmer")