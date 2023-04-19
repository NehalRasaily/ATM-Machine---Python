# ATM with {key : values}

import time

print('Please Enter your card')
time.sleep(2)

detail = {'Nehal': {'pas': 1234, 'balance': 20000}, 'Reeya': {'pas': 6789, 'balance': 50000}}
user_name = list(detail.keys())
name = input('Enter your name: ')
if name in user_name:
    password = int(input('Enter the password: '))

    if password == detail[name]['pas']:

        while True:
            print('''
      1 == Check balance
      2 == Withdraw amount
      3 == Deposit amount
      4 == Exit
      ''')
            try:
                option = int(input('Please select any option: '))
            except:
                print('Invalid option')

            if option == 1:
                balance = detail[name]['balance']
                print(f'Your balance is : {balance}')


            elif option == 2:
                withdrawl = int(input('Enter your Withdraw amount: '))
                detail[name]['balance'] = detail[name]['balance'] - withdrawl

                if detail[name]['balance'] < detail[name]['balance']:
                    print('Insufficient balance!')
                    break
                print("Your update balance is", detail[name]['balance'])

            elif option == 3:
                Deposit1 = int(input("Enter your Deposit amount: "))
                detail[name]['balance'] = detail[name]['balance'] + Deposit1
                print("Your updated balance is", detail[name]['balance'])

            elif option == 4:
                print("Thanks for using our firm")
                break
            else:
                print('Requested option is not available!')
    else:
        print('Password is Incorrect!')
else:
    print('User name is not defined!')
