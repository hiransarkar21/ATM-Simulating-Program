import random
import my_module as backend_file

GUI='''
                        - - - - - - - - - - - - - - - - - - - - - -
                       |                                            |
                       |                                            |
                       |            W E L C O M E  T O              |
                       |   P R I V A T E   B A N K  O F  I N D I A  |
                       |                                            |
                       |                                            |
                       |  Functionality                             |
                       |  - - - - - - -                             |
                       |                                            |
                       |  . Check Balance                           |
                       |  . WithDrawal Of Money                     |
                       |  . Deposition of Money                     |
                       |  . Returning Of Your Card                  |
                       |                                            |
                        - - - - - - - - - - - - - - - - - - - - - -
'''

pins=["1239","0001","3245","9990"]
correct_pin=random.choice(pins)
pin_count=0

print(GUI)

print(" Enter Your Card .")
print(" Card Entered ! ")
print()


def pin_checker_and_overall_functions_performer():
        global correct_pin
        global pin_count
        while True:
                u_input=int(input(" Enter Your 4 Digit Pin : "))
                print()
                if(pin_count == 5):
                        print(" Time Out .")
                        print(" Try Again Later .")
                        print()
                        break
                else:
                        if(u_input == int(correct_pin)):
                                print(" Password Accepted . ")
                                print()
                                print(backend_file.exp_GUI)
                                while True:
                                        u_input_2=int(input(" Enter Your Choice : "))
                                        print()
                                        if(u_input_2 == int(1)):
                                                print()
                                                print(" Fetching Data .. ")
                                                backend_file.check_balance()
                                        elif(u_input_2 == int(2)):
                                                print()
                                                print(" Fetching Data .. ")
                                                backend_file.crediting_process()
                                        elif(u_input_2 == int(3)):
                                                print()
                                                print(" Fetching Data ..")
                                                backend_file.depositing_process()
                                        elif(u_input_2 == int(4)):
                                                print()
                                                backend_file.returning_card_process()
                                        else:
                                                print(" Invaild Input . Please Try Again . ")
                                                print()
                        else:
                                print(" Invalid Pin . Try Again ")
                                print()
                                pin_count+=1

                
     
pin_checker_and_overall_functions_performer()
