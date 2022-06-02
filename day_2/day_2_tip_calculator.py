# day 2: tip calculator

print('Welcome to the tip calculator')
bill = float(input('What was the total bill? $'))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input('How many people to split the bill?'))

total_bill = bill * (1 + tip/100)
bill_per_person = round(total_bill / people,2)
final_amount = '{:.2f}'.format(bill_per_person)  ### float -> string 
print('Each person should pay: ${bill_per_person}')