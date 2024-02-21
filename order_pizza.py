print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size of the pizza you want to try today? S M L\n")
add_paperroni = input("Do you want to add paperroni? Y or N\n")
extra_cheese = input("Do you want to add extra cheese? Y or N\n") #Y or N

bill = 0

if size == 'S':
    bill = 15
elif size == 'M':
    bill = 20
else:
    bill = 25


if add_paperroni == 'Y':
    if size == 'S':
        bill += 2
    if size == 'M':
        bill += 3
    if size == 'L':
        bill += 3

if extra_cheese == 'Y':
    bill += 1
print(f"Your final bill is: ${bill}.")
