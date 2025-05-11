""" Creating a bank management system with python
Components
- type of transaction user wants to make: airtime self, airtime others , data, intra transfer, other banks transfer, change of pin, 
- what comes after each transaction type"""

account_balance = int(input("Enter your current account balance: "))
def check_airtime():
    amt = int(input("Enter amount of airtime wanted:"))
    if account_balance> amt:
            print("Airtime purchase successful")
    elif account_balance< amt:
            print("Insufficient balance")
    else:
            print("Invalid input")

def check_data(amt):
    if account_balance> amt:
            return True
    elif account_balance< amt:
            return False
    else:
            print("Invalid input")

def check_transfer(amt):
    if account_balance> amt:
            print("Transaction successful")
    elif account_balance< amt:
            print("Insufficient balance")
    else:
            print("Invalid input")



def airtime_self():
    while True:
        check_airtime()
        break

def airtime_others():
    while True:
        beneficiaries_num= input("Enter beneficiary's phone number")
        if len(beneficiaries_num)== 11:
            check_airtime()
        else:
             print("Enter a valid phone number")
        break


def data_sub_self():
    while True:
        print("""Choose the data plan you want to buy
              1. 100mb for #100
              2. 100mb for #200
              3. 300mb for #300
              4. 1.5gb for #1000"""
              )
        choice = input("")
        if choice== "1":
            if check_data(100)==True:
                print("Transaction successful")
            else:
             print("Insufficient balance")
        elif choice== "1":
            if check_data(200)==True:
                print("Transaction successful")
            else:
             print("Insufficient balance")
        elif choice== "1":
            if check_data(300)==True:
                print("Transaction successful")
            else:
             print("Insufficient balance")
        elif choice== "1":
            if check_data(1000)==True:
                print("Transaction successful")
            else:
             print("Insufficient balance")
        break
def data_others():
    print("Enter recipient's number")
    num= input()
    if len(num)== 11:
        data_sub_self()
    else:
         print("Invalid phone number")
             
def intra_transfer():
    while True:
        #please enter amount
        #enter recipient's acc num
        print("Enter recipient's account number: ")
        acc_no= input()
        if len(acc_no)== 10:
            print("Please enter amount: " )
            amt= int(input())
            check_transfer(amt)
        else:
            print("Invalid account number")
        break
        

print("WELCOME TO ADENIKE'S BANK MANAGEMENGT SYSTEM :)")
def transaction_type():
     print("""Choose the type of transaction you want: 
      1. Airtime_self
      2. Airtime_others 
      3. Data plan- self
      4. Data plan- others
      5. Transfer""")
transaction_type()
choice= input()
if choice== "1":
    airtime_self()
elif choice=="2":
    airtime_others()
elif choice == '3':
    data_sub_self()
elif choice == '4':
    data_others()
elif choice == '5':
    intra_transfer()
else:
    print("invalid input")
    transaction_type()
    
