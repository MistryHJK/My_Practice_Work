# Here I am defining a directory from which user will choose the operation
calc ={
  1: lambda a,b: a+b,
  2: lambda a,b: a-b,
  3: lambda a,b: a*b,
  4: lambda a,b: a/b,
  5: lambda a,b: a//b,
  6: lambda a,b: a%b,
}
# Taking input from the user
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

#printing the menu
while True:
  try:
    print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Floor Division\n6. Modulus")
    val = int(input("Enter any  number between 1 to 6: "))
    if 1 <= val <= 6:
        break
    else:
        print("Please enter a valid number")

  except ValueError:
    print("Invalid input please enter a valid number")

#printing the result
result = calc[val](a,b)
print(f"Result: {result}")