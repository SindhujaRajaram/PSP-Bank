from create_account import *

print("WELCOME TO PSP BANK\n"
      "1. CREATE ACCOUNT\n"
      "2. VIEW ACCOUNT DETAILS\n"
      "3. WITHDRAW\n"
      "4. DEPOSIT")
choice = int(input("ENTER YOUR CHOICE: "))
if choice == 1:
    acc_details()

elif choice == 2:
    show_details()

elif choice == 3:
    withdraw()

elif choice == 4:
    deposit()
