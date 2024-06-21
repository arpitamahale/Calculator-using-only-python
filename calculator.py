logo = """
 _____________________
|  _________________  |
| |              0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

print(logo)
def add(num1, num2):
  return num1+num2

def substract(num1, num2):
  return num1-num2

def divide(num1, num2):
  return num1/num2

def multiply(num1, num2):
  return num1*num2

def modulus(num1, num2):
  return num1%num2
operations = {
  "+" : "add",
  "-" : "substract",
  "/" : "divide",
  "*" : "multiply",
  "%" : "modulus"
}
def cal_func(num1, num2):
        if operation_symbol == "+":
            return add(num1, num2)
        elif operation_symbol == "-":
            return substract(num1, num2)
        elif operation_symbol == "/":
            return divide(num1, num2)
        elif operation_symbol == "*":
            return multiply(num1, num2)
        else:
            return modulus(num1, num2)
next = True
while next==True:
    
    num1 = float(int(input("What's first number? : ")))
    for symbol in operations:
        print(symbol)
    operation_symbol = input("pick an operation from above line :")
    num2 = float(input("What's second number? : "))
    calculation_function = operations[operation_symbol]
    if num1 == 0 and operation_symbol == "/":
      print("infinite")
    else:
      answer = cal_func(num1, num2)
      print(f"{num1} {operation_symbol} {num2} = {answer}")
    ask_next = input("type 'y' to continue calculation or type 'n' to exit " )
    if ask_next=='y':
        next=True
    else:
        next=False
print("Thank You! \nYou are successfully exit the calculator ")