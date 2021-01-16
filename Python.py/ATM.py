
import time

a = str(input("Type The Name Of The Card Owner By Which This Card Is Registerd\n"))
if a == ("Vivaan41208"):
    time.sleep(2)

    password = 1208
    pin = int(input("Enter You'r Pin\n"))

    balance = 10000

    if pin == password:
        while True:
            print("Welcome")
            print("""
                1 == Balance
                2 == Withdaw Balance
                3 == Deposit Balance
                4 == Quit
                """)
            try:
                option = int(input("Please Enter Your Choise\n"))
            except:
                print("Please Enter Valid Option")

            if option == 1:
                print(f"You'r Current Balance Is {balance}")

            elif option == 2:
                withdraw = int(input("Please The Amount You Want To Withdraw\n"))
                balance = balance - withdraw
                print(f"{withdraw} is Debited From You'r Account")
                print(f"You'r Updated Balance Is {balance}")

            elif option == 3:
                deposit = int(input("Please The Amount You Want To Deposit\n"))
                balance = balance + deposit
                print(f"{deposit} is Credited From You'r Account")
                print(f"You'r Updated Balance Is {balance}")

            elif option == 4:
                exit()    


        else:
            print("Wrong Pin")
            exit()

else:
    print("Sorry,Wrong User\n")
    exit()
