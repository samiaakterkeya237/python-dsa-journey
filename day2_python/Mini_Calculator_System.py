First_number=int(input("Enter the 1st num: "))
Second_number=int(input("Enter the 2st num: "))
Operator=input("Enter the Operator")

if Operator=="+":
    print(First_number+Second_number)

elif Operator=="-":
    print(First_number-Second_number)

elif Operator=="*":
    print(First_number*Second_number)

else:
    print(First_number/Second_number)