print("The Love Calculator is calculating your score...")
name1 = input("Enter the first name \n") # What is your name?
name2 = input("Enter the second name \n") # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
true_count = 0
love_count = 0
#combined the given two names
combined_namename = name1 + name2
true_word = "TRUE"
love_word = "LOVE"

#convert everything in lower case
to_lowers = combined_namename.lower()

to_lowers_true = true_word.lower()
to_lowers_love = love_word.lower()

for char in to_lowers:
    for t in to_lowers_true:
        if char == t:
            true_count += 1

for char in to_lowers:
    for l in to_lowers_love:
        if char == l:
            love_count += 1
final_score = str(true_count) + str(love_count)
final_score_int = int(final_score)
if final_score_int < 10 or final_score_int > 90:
    print(f"Your score is {final_score_int}, you go together like coke and mentos.")
elif final_score_int > 40 and final_score_int < 50:
    print(f"Your score is {final_score_int}, you are alright together.")
else:
    print(f"Your score is {final_score_int}.")
