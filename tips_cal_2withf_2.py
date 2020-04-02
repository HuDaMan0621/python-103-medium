"""# Allow the ability to divide the check into a equal parts amount a number of people. 
# The user will enter the number of people to be divided amongst. Example session:

# $ python3 tip_calc2.py
# Total bill amount? 100
# Level of service? good
# Split how many ways? 5
# Tip amount: $20.00
# Total amount: $120.00
# Amount per person: $24.00

# Hints:

# Remember that you need to convert the input from the user input to floats instead of ints. Use the float function instead of the int function.
# To format a float number as a dollar value, use Python's formatting syntax: "%.2f" % amount
"""
total_bill = int(input('Total Bill Amount?:$ '))
level_service = input('Level of Service? please enter good, fair or bad ')
good = float(.20)
fair = float (.15)
bad = float (.10)
while level_service == 'good':
    total_bill = (total_bill+(total_bill * good))
    sum = f'your total bill is $ {float(total_bill)}' 
    # {float(total_bill)}'
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

dollar_value = total_bill
print(" Total Bill = ${:.2f}".format( dollar_value ))


# print (total_bill)
split = int(input ('Split in how many ways? '))

total = (total_bill / split)
print(" Total Bill = ${:.2f}".format( total ))



#subject = f'you entered, {student_subject}' 
# greeting = f'hi {name}!!!!!'

# answer = ''
# while answer != "yes":    
#     answer = input('But I really want to! Can I?! ')    
#     answer = answer.lower()
#     print('Thanks!')