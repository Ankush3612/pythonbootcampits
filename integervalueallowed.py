def inputIntegerOnly(num):
  while True:
      user_input = input(num)
      if user_input.isnumeric():
          return user_input
      else:
          print("Invlid input. Please enter integer only")
num = inputIntegerOnly("Enter your num")
print(f"Hello, {num}")
          