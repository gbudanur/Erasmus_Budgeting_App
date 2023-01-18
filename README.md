# Erasmus Budgeting App / Erasmus Bütçe Planlama Uygulaması

This is a basic budget planning app developed to be used by semester abroad (Erasmus) students. Since I started this project with a momentary fad and don't have the motivation to perfect it, it might include basic bugs. In order to avoid most of them I would suggest being careful with the inputs. ***This application does NOT need internet access, it uses local_simple_database library which simply saves anything to a .txt file on your computer. Please do review the code before using it.***

## Features
### • Track records of your assets

By using the "Deposit" option, have your different assets from different bank accounts under one roof. Use "Withdraw" option after spending money. 

### • Get monthly budget expectations

Set your planned monthly income (scholarship, allowance) and spending (rent, monthly subscriptions) from relevant options as well as your remaining duration of mobility (from "Settings") at the beginning of a month and receive monthly budget expectations. _(Math behind it might need an update, use it with caution)_

### • Plan your trips!

From "Travel Planning", set a name for your trip and determine the budget for it. Withdraw money as you spend it. 

### • History

Records of your deposit and withdrawals can be accessed from "History" page. History records of your trips are accessible under the relevant menu.

## Usage

### • Run [main.exe](https://github.com/gbudanur/Erasmus-Budgeting-App/blob/main/main.exe)

### • Do not force the app to shut down. Use "Exit" option. If the app starts crashing on start, delete "int_counter.txt" from the folder "local_simple_database".

### • Directly access data from .txt files located in the folder "local_simple_database"

