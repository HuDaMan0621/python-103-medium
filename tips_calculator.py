# 1. Tip Calculator
# Your task is to write a program that calculates how much of a tip to leave at a restaurant.

# Prompt the user for two things:

# The total bill amount
# The level of service, which can be one of the following: good, fair, or bad
# Calculate the tip amount and the total amount (bill amount + tip amount). The tip percentage based on the level of service is based on:

# good -> 20%
# fair -> 15%
# bad -> 10%

# $ python3 tip_calc.py
# Total bill amount? 100
# Level of service? good
# Tip amount: $20.00
# Total amount: $120.00
# $ python3 tip_calc.py
# Total bill amount? 48
# Level of service? bad
# Tip amount: $4.80
# Total amount: $52.80
# Hints:

# Remember that you need to convert the input from the user input to floats instead of ints. Use the float function instead of the int function.
# To format a float number as a dollar value, use Python's formatting syntax: "%.2f" % amount

total_bill = int(input('Total Bill Amount?:$ '))
level_service = input('Level of Service? please enter good, fair or bad ')
good = float(.20)
fair = float (.15)
bad = float (.10)
while level_service == 'good':
    total_bill = (total_bill+(total_bill * good))
    sum = f'your total bill is $ {float(total_bill)}'
    print (sum)
    break

while level_service == 'fair':
    total_bill = (total_bill+(total_bill * fair))
    sum = f'your total bill is $ {float(total_bill)}'
    print (sum)
    break

while level_service == 'bad':
    total_bill = (total_bill+(total_bill * bad))
    sum = f'your total bill is $ {float(total_bill)}'
    print (sum)
    break

#subject = f'you entered, {student_subject}' 
# greeting = f'hi {name}!!!!!'

# answer = ''
# while answer != "yes":    
#     answer = input('But I really want to! Can I?! ')    
#     answer = answer.lower()
#     print('Thanks!')