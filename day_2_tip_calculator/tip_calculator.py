# This program calculates the tip of a bill


print("Welcome to the tip calculator")

total_bill = float(input("What was the total bill? "))
percent_tip = float(input("What percentage tip would you like to give? 10, 12, 15? "))
num_of_people = float(input("How many people split the bill? "))


raw_split = total_bill / num_of_people
tip_amount = raw_split * (percent_tip / 100)
split_total = round(raw_split + tip_amount, 2)

print(f"Each person should pay {split_total}")
