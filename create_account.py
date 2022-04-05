import random
import sqlite3

connection = sqlite3.connect('accdetails.db')
cursor = connection.cursor()


def acc_details():
    command1 = " CREATE TABLE IF NOT EXISTS " \
               "account(Account_no INTEGER PRIMARY KEY, Cust_name TEXT, bal FLOAT)"
    cursor.execute(command1)
    name = input("Enter your name: ")
    ac_no = random.randint(400000, 5000000)
    print("Your Account number:", ac_no)
    bal = int(input(" Enter the amount you want to deposit: "))
    add = "INSERT INTO account (Account_no,Cust_name, bal) VALUES(?, ?, ?)"
    cursor.execute(add, (ac_no, name, bal))
    print("YOUR ACCOUNT IS CREATED\n")
    connection.commit()


def show_details():
    no = int(input("Enter the Account number: "))
    cursor.execute("SELECT * FROM account WHERE Account_no=?", (no,))
    result = cursor.fetchone()
    for no in result:
        print(no)


def withdraw():
    no = int(input("Enter your Account number: "))
    amount = int(input("Enter the amount: "))
    cursor.execute("SELECT bal FROM account WHERE Account_no=?", (no,))
    old_bal = cursor.fetchone()
    old = float('.'.join(str(ele) for ele in old_bal))
    new_bal = old - amount
    cursor.execute("UPDATE account SET bal=? WHERE Account_no=?",(new_bal,no,))
    print("Your new balance= ", new_bal)
    connection.commit()


def deposit():
    no = int(input("Enter your Account number: "))
    amount = int(input("Enter the amount: "))
    cursor.execute("SELECT bal FROM account WHERE Account_no=?", (no,))
    old_bal = cursor.fetchone()
    old = float('.'.join(str(ele) for ele in old_bal))
    new_bal = old + amount
    cursor.execute("UPDATE account SET bal=? WHERE Account_no=?", (new_bal, no,))
    print("Your new balance= ", new_bal)
    connection.commit()

