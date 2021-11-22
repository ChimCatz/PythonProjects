# Day 2 Project: Tip Calculator
print("Hello, ChiggaHaxlord here! :)")
print("Welcome to the tip calculator.")
total_bill = input("What was the total bill? ")
percent_tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")
#Each person should pay:
percent_tip = float(percent_tip) / 100
payment = round((float(total_bill) + (float(total_bill) * percent_tip)) / int(people), 2)
print(f"If the bill was ${float(total_bill)}, split between {people} people, with {percent_tip * 100}% tip.")
print(f"Each person should pay: ${payment}")