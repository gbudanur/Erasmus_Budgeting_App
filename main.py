# -*- coding: utf-8 -*-
import datetime
from local_simple_database import LocalSimpleDatabase

db = LocalSimpleDatabase()
ctime = datetime.datetime.now()
counter = db["int_counter"]
db["int_counter"] += 1


def tutorial():
    print("--------")
    print(
        "This app is designed to help you keep track of your money during your Erasmus mobility. You will be able to calculate your approximate monthly budget, see your savings and spendings from one place and plan your trips."
    )
    print("--------")
    print(
        "Since this is your first time using the app, you will be asked to enter your duration of mobility, total savings and expected monthly income and spending. You will be able deposit and withdraw money and change the settings for monthly income and spending."
    )
    print("--------")
    print(
        "Please note that, due to my inadequacy in both coding and economy, you are expected to start using this app in the beginning of a month to receive monthly budget expectations."
    )
    print("--------")
    print(
        "However, you can still use the app to keep track of your spendings, at the end of each day, you can enter your spendings and the app will calculate your balance and save it for you. You can also deposit money at any time."
    )
    print("--------")
    print(
        "Please visit 'History' page to access your balance history. You can also reset your data at any time from 'Settings' menu."
    )
    print("--------")
    print(
        "Final note: This app only accepts integer or float inputs. Please enter your values without any currency symbols."
    )
    return ()


def soption1():
    print("--------")
    print(
        "Enter the remaining duration of your mobility in months (Please change it every month) (0 to leave) Currently: "
        + db["str_duration"]
    )
    print("--------")
    endmobility = str(input(":"))
    if endmobility == "0":
        settings()
    db["str_duration"] = endmobility
    print("--------")
    print("Remaining duration of your mobility: " + db["str_duration"] + " months")
    print("--------")
    main()


def settings():
    print("--------")
    print(
        "Settings: Duration of mobility (1), Tutorial (2), Reset data (3), Manual reset (4), Exit (0)"
    )
    print("--------")
    option = 1
    while option != "0":
        option = str(input(":"))
        while type(option) != str and (option != "1" or option != "2"):
            print("--------")
            print("Please enter a valid number")
            print("--------")
            option = float(input(":"))
        if option == "1":
            soption1()
            option = 0
        elif option == "2":
            tutorial()
            option = 0
        elif option == "3":
            print("--------")
            print("Are you sure you want to reset all data? (Y/N)")
            print("--------")
            yesno = input(":")
            if yesno == "Y":
                db["float_balance"] = 0
                db["float_mincome"] = 0
                db["float_mspending"] = 0
                db["int_counter"] = 0
                db["str_history"] = "Reset "
                db["str_duration"] = "0"
                print("--------")
                print("Data reset")
                print("--------")
                option = 0
            elif yesno == "N":
                print("--------")
                print("Data is untouched")
                print("--------")
                option = 0
        elif option == "4":
            deletext = 1
            while deletext != "0":
                delete = input(
                    "Enter the name of the data you want to delete: format_name (float_mincome), type '0' to leave"
                )
                if delete == "0":
                    deletext = "0"
                else:
                    db[delete] = ""
            option = 0

    main()


def deposit():
    depositamount = 1
    while depositamount != 0:
        print("--------")
        print("Deposit: Enter the amount you would like to deposit, type '0' to leave")
        print("--------")
        depositamount = float(input(":"))
        while depositamount < 0 or type(depositamount) != float:
            print("--------")
            print("Please enter a valid number")
            print("--------")
            depositamount = float(input(":"))
        db["float_balance"] += float(depositamount)
        db["str_history"] += "\n +" + str(depositamount) + " " + str(ctime)
        print("--------")
        print("Current balance: " + str(db["float_balance"]))

    main()


def withdraw():
    withdrawamount = 1
    while withdrawamount != 0:
        print("--------")
        print(
            "Withdraw: Enter the amount you would like to withdraw, type '0' to leave"
        )
        print("--------")
        withdrawamount = float(input(":"))
        while withdrawamount < 0 or type(withdrawamount) != float:
            print("--------")
            print("Please enter a valid number")
            print("--------")
            withdrawamount = float(input(":"))
        db["float_balance"] -= float(withdrawamount)
        db["str_history"] += "\n -" + str(withdrawamount) + " " + str(ctime)
        print("--------")
        print("Current balance: " + str(db["float_balance"]))

    main()


def balance():
    print("--------")
    print("Current balance: " + str(db["float_balance"]))
    budget()
    print("--------")
    main()


def monthlyincome():
    mincome = 1
    while mincome != 0:
        print("--------")
        print("Monthly Incomes: Enter your monthly incomes, type '0' to leave")
        print("--------")
        mincome = float(input(":"))
        while mincome < 0 or type(mincome) != float:
            print("--------")
            print("Please enter a valid number")
            print("--------")
            mincome = float(input(":"))
        db["float_mincome"] += float(mincome)
        print("--------")
        print("Current monthly income: " + str(db["float_mincome"]))
        print("--------")
    main()


def monthlyspending():
    mspending = 1
    while mspending != 0:
        print("--------")
        print("Monthly Spendings: Enter your monthly spendings, type '0' to leave")
        print("--------")
        mspending = float(input(":"))
        while mspending < 0 or type(mspending) != float:
            print("--------")
            print("Please enter a valid number")
            print("--------")
            mspending = float(input(":"))
        db["float_mspending"] -= float(mspending)
        print("--------")
        print("Current monthly spending: " + str(db["float_mspending"]))

    main()


def existingtravel(travelchoice):
    traveloption = 1
    while traveloption != "0":
        print("--------")
        print("Current trip: " + travelchoice)
        print("Balance for the trip: " + str(db["float_balance" + travelchoice]))
        print(travelchoice + ": Deposit (1), Withdraw (2), History (3), Exit (0)")
        print("--------")
        traveloption = str(input(":"))
        if traveloption == "1":
            traveldeposit = 1
            while traveldeposit != 0:
                print("--------")
                print(
                    "Deposit: Enter the amount you would like to deposit, type '0' to leave"
                )
                print("--------")
                traveldeposit = float(input(":"))
                while traveldeposit < 0 or type(traveldeposit) != float:
                    print("--------")
                    print("Please enter a valid number")
                    print("--------")
                    traveldeposit = float(input(":"))

                db["float_balance" + travelchoice] += float(traveldeposit)
                db["str_history" + travelchoice] += (
                    "\n +" + str(traveldeposit) + " " + str(ctime)
                )
                print("--------")
                print("Current balance: " + str(db["float_balance" + travelchoice]))

        elif traveloption == "2":
            travelwithdrawal = 1
            while travelwithdrawal != 0:
                print("--------")
                print(
                    "Withdraw: Enter the amount you would like to withdraw, type '0' to leave"
                )
                print("--------")
                travelwithdrawal = float(input(":"))
                while travelwithdrawal < 0 or type(travelwithdrawal) != float:
                    print("--------")
                    print("Please enter a valid number")
                    print("--------")
                    traveloption = float(input(":"))

                db["float_balance" + travelchoice] -= float(travelwithdrawal)
                db["str_history" + travelchoice] += (
                    "\n -" + str(travelwithdrawal) + " " + str(ctime)
                )
                print("--------")
                print("Current balance: " + str(db["float_balance" + travelchoice]))

        elif traveloption == "3":
            print("--------")
            print("History: " + db["str_history" + travelchoice])
            print("--------")
    travelassist()


def newtravel(travelchoice):
    db["str_travels"] += ", " + travelchoice
    db["str_" + travelchoice] = travelchoice + " Travel created on " + str(ctime)
    traveloption = 1
    while traveloption != "0":
        print("--------")
        print("New trip: " + travelchoice)
        print("Balance for the trip: " + str(db["float_balance" + travelchoice]))
        print(travelchoice + ": Deposit (1), Withdraw (2), History (3), Exit (0)")
        print("--------")
        traveloption = str(input(":"))
        if traveloption == "1":
            traveldeposit = 1
            while traveldeposit != 0:
                print("--------")
                print(
                    "Deposit: Enter the amount you would like to deposit, type '0' to leave"
                )
                print("--------")
                traveldeposit = float(input(":"))
                while traveldeposit < 0 or type(traveldeposit) != float:
                    print("--------")
                    print("Please enter a valid number")
                    print("--------")
                    traveldeposit = float(input(":"))

                db["float_balance" + travelchoice] += float(traveldeposit)
                db["str_history" + travelchoice] += (
                    "\n +" + str(traveldeposit) + " " + str(ctime)
                )
                print("--------")
                print("Current balance: " + str(db["float_balance" + travelchoice]))

        elif traveloption == "2":
            travelwithdrawal = 1
            while travelwithdrawal != 0:
                print("--------")
                print(
                    "Withdraw: Enter the amount you would like to withdraw, type '0' to leave"
                )
                print("--------")
                travelwithdrawal = float(input(":"))
                while travelwithdrawal < 0 or type(travelwithdrawal) != float:
                    print("--------")
                    print("Please enter a valid number")
                    print("--------")
                    traveloption = float(input(":"))

                db["float_balance" + travelchoice] -= float(travelwithdrawal)
                db["str_history" + travelchoice] += (
                    "\n -" + str(travelwithdrawal) + " " + str(ctime)
                )
                print("--------")
                print("Current balance: " + str(db["float_balance" + travelchoice]))

        elif traveloption == "3":
            print("--------")
            print("History: " + db["str_history" + travelchoice])
            print("--------")
    travelassist()


def travelassist():
    print(db["str_travels"])
    print("--------")
    print(
        "Please set a name for your trip or enter the trip you would like to access, type '0' to leave"
        + " current trips: "
        + db["str_travels"]
    )
    print("--------")
    travelchoice = str(input(":"))
    if travelchoice == "0":
        main()
    if db["str_" + travelchoice] != "":
        existingtravel(travelchoice)
    else:
        newtravel(travelchoice)


def history():
    print("--------")
    print("History: " + db["str_history"])
    print("--------")
    main()


def budget():
    budgetbalance = (
        (db["float_balance"] / float(db["str_duration"]))
        + db["float_mincome"]
        - db["float_mspending"]
    )
    print("Monthly budget is: " + str(budgetbalance))


def main():
    print("--------------------")
    print(
        "Choose an option: SETTINGS (1), DEPOSIT (2), WITHDRAW (3), MONTHLY INCOMES (4), MONTHLY SPENDINGS (5), BALANCE (6), HISTORY (7), TRAVEL PLANNING (8), EXIT (9)"
    )
    print("--------------------")
    firstopt = str(input(":"))
    while (
        firstopt != "1"
        and firstopt != "2"
        and firstopt != "3"
        and firstopt != "4"
        and firstopt != "5"
        and firstopt != "6"
        and firstopt != "7"
        and firstopt != "8"
        and firstopt != "9"
    ):
        print("--------")
        print("Please enter a valid number")
        print("--------")
        firstopt = str(input(":"))
    if firstopt == "1":
        settings()
    elif firstopt == "2":
        deposit()
    elif firstopt == "3":
        withdraw()
    elif firstopt == "4":
        monthlyincome()
    elif firstopt == "5":
        monthlyspending()
    elif firstopt == "6":
        balance()
    elif firstopt == "7":
        history()
    elif firstopt == "8":
        travelassist()
    elif firstopt == "9":
        exit()


print("Welcome to Erasmus Budgeting App")

if counter < 1:
    print("--------")
    print(
        "This is your first time using the app, type '1' to recevie the beginner's guide (highly recommended), type '0' to skip. Have an amazing Erasmus experince!"
    )
    choicefortutorial = float(input(":"))
    while choicefortutorial != 0 and choicefortutorial != 1:
        print("--------")
        print("Please enter a valid number")
        print("--------")
        choicefortutorial = float(input(":"))
    if choicefortutorial == 1:
        tutorial()
    elif choicefortutorial == 0:
        print("--------")
        print("You can always access the tutorial from 'Settings' menu")
        print("--------")
        main()
    soption1()

budget()
main()
