# ATM Simulating Program

import sys

current_balance=12342

# GUI explaining which key does which function -----

exp_GUI='''
                   - - - - - - - - - - - - - - - 
                 |                              |
                 | Key Functionality            |
                 | - - - - - - - - -            |
                 |                              |
                 | . 1 for Checking Balance     |
                 | . 2 for WithDrawling Process |
                 | . 3 for Depositing Process   |
                 | . 4 for Returning Card       |
                 |                              |
                  - - - - - - - - - - - - - - -
'''

# Main ATM Simulating Functions --------    
def check_balance():
    print(" Current Balance is $ {}".format(current_balance))
    print()


def crediting_process():
    default_input=int(input(" Enter Amount To Be WithDrawled : "))
    print()
    global current_balance
    current_balance -= default_input
    print(" WithDrawl Of Amount {} Was Successfull .".format(default_input))
    print(" Current Balance is {} .".format(current_balance))
    print()
    

def depositing_process():
    default_input=int(input(" Enter Amount To Be Credited : "))
    print()
    global current_balance
    current_balance += default_input
    print(" Deposition of Amount {} Was Successful .".format(default_input))
    print(" Current Balance is {} .".format(current_balance))
    print()

def returning_card_process():
    print(" Returning Card . Please Wait . ")
    print(" Your Card Has Been Ejected . Thank You For Using our Service .")
    print()
    exit()
# Main Functions Ended --------
