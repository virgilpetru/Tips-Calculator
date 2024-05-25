print("Welcome to the tip calculator.")
bill = input("What was the total bill? ")
tip = input("What percentage would you like to give? 10, 12. or 15? ")
people = input("How many people to split the bill? ")
bill = float(bill)
tip = int(tip)
people = int(people)
tip1 = (tip / 100) * bill
total_bill = (tip1 + bill) / people
bill_final = format(total_bill,".2f")
print(bill_final)