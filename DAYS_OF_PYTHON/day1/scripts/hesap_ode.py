# version 1
"""print("Welcome to the tip calculator!")
bill = float(input("What was the total bill in TL? "))
tip = int(input("How much tip (in percent) would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(final_amount)

print(f"Each person should pay: {final_amount} TL")"""

# version 2
import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(",")

result_index = random.randint(0, len(names)-1)

print("%s will pay the bill." % names[result_index])

# random.choice çözümü
# print("%s will pay the bill." % random.choice(names))



