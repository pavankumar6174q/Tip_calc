print('Welcoe to tip calculator.')
bill = float(input('Enter your bill amount\n'))
tip = int(input('How much tip do you ean to give 10,12 or 15?\n'))
people =float(input('How many people are there to split the bill\n'))
tip_per = tip/100
total_bill = bill*tip_per
to_pay = total_bill/people +bill
print(f'each person should pay ${to_pay}')