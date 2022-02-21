import time
print("Hello World !")
time.sleep(1)
print("Welcome to the tip calculator")
print("$$$")
time.sleep(1)

enter_bill=float(input("Enter the bill total :\n"))

select_tip=input(" Enter 10, 15, or  20 to calculate your tip based on your percentage :\n")

if select_tip=='10':
    decimal_ten=(.10)
    func_tion=(enter_bill*decimal_ten)
    total_bill=(enter_bill+func_tion)
    print("Your bill will be :"+" "+ (str(total_bill))+" "+"Have a nice day !")
elif select_tip=='15':
    decimal_fiftn=(.15)
    func_tion=(enter_bill*decimal_fiftn)
    total_bill=(enter_bill+func_tion)
    print("Your bill will be :"+" "+ (str(total_bill))+" "+"Have a great day !")
elif select_tip=='20':
    decimal_twnty=(.20)
    func_tion=(enter_bill*decimal_twnty)
    total_bill=(enter_bill+func_tion)
    result_string=("Your bill will be:"+" "+(str(total_bill))+" "+"Have a wonderful day !")
    print(result_string)

enter_key_exit=input("Press ANY key to exit the program:\n")
# made by nanofaradhenry studios
### thanks for looking





