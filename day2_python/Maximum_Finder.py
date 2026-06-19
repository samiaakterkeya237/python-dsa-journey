num1=int(input("Num1:"))
num2=int(input("Num2:"))
num3=int(input("Num3:"))

if num1>num2 & num1>num3:
    print(f'Largest number is {num1}')
elif num2>num1 & num2>num3:
     print(f'Largest number is {num2}')
else:
    print(f'Largest number is {num3}')