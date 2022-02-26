#A calculator program that performs basic arithmetic operations
#from calculator_art import logo
  #add
def add(n1, n2):
    return n1 + n2

  #subtract
def subtract(n1, n2):
    return n1 - n2

  #multiply
def multiply(n1, n2):
    return n1 * n2

  #divide
def divide(n1, n2):
    return n1 / n2


operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide
}
def calculator():
  #print(logo)
  do_calculation = True
  num1 = float(input("what is the first number: "))

  for operation in operations:
    print(operation)
  while do_calculation:
    symbol = input("pick an operation from the line above: ")
    num2 = float(input("what is the next number: "))
 
    calculation = operations[symbol]
    answer = calculation(num1, num2)
    print(f"{num1} {symbol} {num2} = {answer} ")


    to_continue = input ("do you want to continue, 'y' or 'n' ").lower()
    if to_continue == "y":
      num1 = answer
      do_calculation
    else:
      do_calculation = False
      calculator()
calculator()