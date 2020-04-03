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

#display the current value of coins in hand


# #ask the user if he/she wants a coin, if answer is yes, add a coin and display the value

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
