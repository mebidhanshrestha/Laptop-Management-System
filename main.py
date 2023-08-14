import read
import operation

# This is the main file 
read.welcome()
loop = True

while loop:
    read.select_option()

    select_option = False
    while not select_option:
        try:
            select = int(input("Enter an option: "))
            select_option = True
        except:
            read.invalid()
            read.select_option()
    if select == 1:

        operation.purchase()
    elif select == 2:
        operation.sell()
    elif select == 3:
        read.thanks()
        loop = False
    else:
        read.invalid()
