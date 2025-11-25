# OOP format basic Calculator

class Calculator:
    
    # arithmetic methods
    def add(self, x, y):
        return x + y
    
    def sub(self, x, y):
        return x - y
    
    def mul(self, x, y):
        return x * y
    
    def divide(self, x, y):
        if y == 0:
            return "Can't devided by Zero"
        return x / y
    
    # A. Add a menu() method
    def menu(self):
        print("\n" + "=" * 40)
        print("Basic OOP Calculator")
        print("=" * 40)
        print("Enter 1 for Addition")
        print("Enter 2 for Subtract")
        print("Enter 3 for Multiply")
        print("Enter 4 for Divide")
        print("Enter 5 for Exit")
        print("=" * 40)
    
    def input_control(self, user_data):
        while True:
            try:
                return float(input(user_data))
            except ValueError:
                print("Invalid input! Please enter a valid number")
                
    # B. Add a run() method
    def run(self):
        while True:
            self.menu()
            pick = input("Enter the number from the list above: ")
            
            if pick == "5":
                print("Thanks for using Basic Calculator!")
                break
            
            if pick not in ["1", "2", "3", "4"]:
                print("Invalid number!\nEnter the number from the list above")
                continue
            
            num1 = self.input_control("Enter first number: ")
            num2 = self.input_control("Enter second number: ")
            
            print("-" * 40)
            
            if pick == "1":
                print(f"Addition result is: {num1} + {num2} = {self.add(num1,num2)}")
                
            elif pick == "2":
                print(f"Subtract result is: {num1} - {num2} = {self.sub(num1,num2)}")
                
            elif pick == "3":
                print(f"Multiply result is: {num1} * {num2} = {self.mul(num1,num2)}")
            
            elif pick == "4":
                print(f"Divided result is: {num1} / {num2} = {self.divide(num1,num2)}")
                

# C. Create a Calculator object
obj = Calculator()
obj.run()