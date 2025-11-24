import cal_func
from cal_func import add, sub, mul, divided

while True:
    cal_func.show_menu()
    pick = input("Pick a number (1-5): ")
    
    if pick == "5":
        print("Calculater Exit!\nThanks for using basic calculator!")
        break
        
    if pick not in ["1", "2", "3", "4"]:
        print("Invalid Pick!\nPlease pick a number in range 1-5")
        continue
        
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except:
        print("Please enter only number.")
        continue
    
    if pick == "1":
        print(f"Addition result is: {num1} + {num2} = {add(num1,num2)}")
        
    if pick == "2":
        print(f"Subtraction result is: {num1} - {num2} = {sub(num1,num2)}")
        
    if pick == "3":
        print(f"Multiplication result is: {num1} * {num2} = {mul(num1,num2)}")
        
    if pick == "4":
        print(f"Division result is: {num1} / {num2} = {divided(num1,num2)}")