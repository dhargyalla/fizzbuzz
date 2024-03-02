#Fizz Buzz Game
#Rule : if a number is divisible by both 3 and 5, Then print FizzBuzz instead of printing the number itself
#       if a number is divisible by 3, then print Fizz instead of printing the number itself
#       if a number is divisible by 5, then print Buzz instead of printining the number itself

for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
