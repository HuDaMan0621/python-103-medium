# #3. How many coins?
# Write a program that will prompt you for how many coins you want. Initially you have no coins. It will ask you if you want a coin? If you type "yes", it will give you one coin, and print out the current tally. If you type no, it will stop the program. Example run:

# $ python3 coins.py
# You have 0 coins.
# Do you want another? yes
# You have 1 coins.
# Do you want another? yes
# You have 2 coins.
# Do you want another? no
# Bye

# count = 0
# groceries = ''
# while count < 3:    
#     groceries = groceries + input('What do you need from the store today? ')    
#     groceries = groceries + '\n'# Add a line break after each grocery item    count = count + 1print(f'Here is your grocery list:\n{groceries}')


#display the current value of coins in hand
# count = 0
# coin = int(count)
# any = f'you have {int(coin)} coins'
# print (any)

# #ask the user if he/she wants a coin, if answer is yes, add a coin and display the value
# answer = ''
# while answer != 'no':
#     answer = input('do you want a coin? ')
#     # total_coin = count + f'{input(1)}'
#     anwer = answer.lower()
#     print ('ok')

# #ask the user if he/she wants a coin, if answer is yes, add a coin and display the value
count = 1

answer = input('do you want a coin? ')
while answer == 'yes':  
    print (f'You have {count} coin(s).')
    answer = input('do you want another one? ') 
    if (answer == 'yes'): 
        count = count + 1

print('ok!')

#when user say no, exit program 
    

# count = 0
# coin = int(count) 

# any = f'you have {int(coin)} coins'
# print (any)
# answer = ''
# while answer == 'yes':
#     answer = input('do you want another?')
#     coin = count + 1
#     sum = coin
#     print (sum)

#     if answer == 'no':
#             non = f' you now have {sum}, coins'
#             break
#     else: count = coin + 1

# print ()

# answer = ''
# while answer != "yes":    
#     answer = input('But I really want to! Can I?! ')    
#     answer = answer.lower()
#     print('Thanks!')