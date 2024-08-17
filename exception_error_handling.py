while True:
  try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
  except Exception as message:
    print(f"Error message: {num1}")
  else:
    break
print(f"{num1} divided by {num2} is {result}")
