#If the bill was $150.00, split between 5 people, with 12% tip. 
bill_amt = 150
people = 5
tip = 120/100
#Each person should pay (150.00 / 5) * 1.12 = 33.6
per_person = (bill_amt / people) * tip
print(round(per_person))
