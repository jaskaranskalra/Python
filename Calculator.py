# In[41]:


def calculate():
    Number_1 = int(input('Enter your first number: '))
    Number_2 = int(input('Enter your second number: '))
    operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')
    if operation == '+':
        #Addition
        print ('{} + {} = '.format(Number_1, Number_2))
        print (Number_1 + Number_2)

    elif operation == '-':
        #Substraction
        print ('{} - {} = '.format(Number_1, Number_2))
        print (Number_1 - Number_2)

    elif operation == '*':
        #Multiplication
        print ('{} * {} = '.format(Number_1, Number_2))
        print (Number_1 * Number_2)

    elif operation == '/':    
        #Division
        print ('{} / {} = '.format(Number_1, Number_2))
        print (Number_1 / Number_2)

    else:
        print ('Operator types is not a valid operator, please run the program again.')
    
    calculate_again()
    
def calculate_again():
    # new input from user
    calc_again = input('''Do you want to calculate again?
    Please type Y for Yes or N for No.''')
    
    if calc_again.upper() == 'Y':
        calculate()
    
    elif calc_again.upper() == 'N':
        print('Thanks for using the program. See you again!')

    else:
        calculate_again()


# In[42]:


calculate()

