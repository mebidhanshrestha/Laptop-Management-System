import read
import write
def valid_id_sell(mainData):
    """
        This function checks if the ID entered is valid or not.
        If the ID is not valid, an invalid message is shown.
        Takes the dictionary as a parameter.
        Returns the valid ID.
    """
    valid_data = False
    while valid_data == False:
        try:
            # print(mainData)
            ID = int(input("Enter the ID of the laptop you want to sell: "))
            if 0 < ID <= len(mainData):  # ID should be greater than 0 and less than or equal to the length of the
                # dictionary
                if int(mainData[ID][3]) > 0:
                    valid_data = True
                    return ID
                else:
                    read.out_of_stock()
            else:
                read.invalid()
        except:
            read.invalid()


def valid_quantity_sell(mainData, ID):
    """ This function checks if the quantity of the laptop is available or not """
    valid_quan = False
    while valid_quan == False:
        try:
            quantity = int(input("How many pieces do you want to sell? "))
            if quantity > 0 and quantity <= int(mainData[ID][3]):
                valid_quan = True
                return quantity
            else:
                read.range()
        except:
            read.invalid()


def sell():
    """ This function is the main function that sell the laptops.
        A 2D list is created which holds the ID and quantity of the laptops.
        The user is asked if he wants to Laptop more laptops.
        A function to print and write the bill is called.
    """
    print("\n Let's sell a laptop. \n")

    file_contents = write.read_file()
    mainData = write.dictionary(file_contents)

    cart = []
    write.print_laptop(mainData)
    continueLoop = True  # assigning boolean value to a variable
    while continueLoop:  # outerloop

        Id = valid_id_sell(mainData)
        if int(mainData[Id][3]) <= 0:
            read.range()
            continueLoop = False
        else:
            read.available()
            qn = valid_quantity_sell(mainData, Id)
            mainData[Id][3] = int(mainData[Id][3]) - qn
            cart.append([Id, qn])

        write.write_file(mainData)
        write.print_laptop(mainData)

        more = True
        while more:  # innerloop
            userInput = input("Do you want to buy or sell more laptops?(yes/no) ")

            if userInput.lower() == "no":
                continueLoop = False  # outerloop is terminated, bill details will be asked
                more = False  # innerloop is terminated

            elif userInput.lower() == "yes":
                continueLoop = True  # outerloop continues, more Laptops will be Laptoped
                more = False  # innerloop is terminated

            else:
                read.invalid()
                more = True  # innerloop continues

    print()
    write.sell_bill(cart)  # function to print and write the bill
    read.sell()

def valid_id_sell(mainData):
    """
        This function checks if the ID entered is valid or not.
        If the ID is not valid, an invalid message is shown.
        Takes the dictionary as a parameter.
        purchases the valid ID.
    """
    valid_id = False
    while not valid_id:
        try:
            ID = int(input("Enter the ID of the Laptop: "))
            if ID > 0 and ID <= len(mainData):
                valid_id = True
                return ID
            else:
                read.invalid()
        except ValueError:
            read.invalid()


def valid_quantity_purchase():
    """
        This function checks if the quantity entered is valid or not i.e. quantity is more than 0.
        purchases Quantity of the Laptops to be purchaseed
    """
    valid_quan = False
    while not valid_quan:
        try:
            quantity = int(input("How many pieces do you want to purchase? "))
            if quantity > 0:
                valid_quan = True
                return quantity
            else:
                read.invalid()
        except ValueError:
            read.invalid()


def purchase():
    """ This function is the main function that purchase the laptop.
        A list is created which holds the ID and quantity of the laptop.
        The user is asked if he wants to purchase more laptop.
        A function to print and write the bill of the purchaseed is called.
    """
    print("\n Let's purchase a laptop. \n")

    file_contents = write.read_file()
    mainData = write.dictionary(file_contents)

    cart = []
    continueLoop = True
    while continueLoop:  # outerloop
        write.print_laptop(mainData)  # list of laptop is printed
        Id = valid_id_sell(mainData)
        qn = int(valid_quantity_purchase())
        mainData[Id][3] = int(mainData[Id][3]) + qn
        cart.append([Id, qn])

        write.write_file(mainData)
        write.print_laptop(mainData)

        more = True
        while more == True:  # inner loop
            userInput = input("Do you want to buy or sell more laptop?(yes/no) ")
            if userInput.lower() == "no":
                continueLoop = False  # outerloop is terminated, bill details will be asked
                more = False  # inner loop is terminated

            elif userInput.lower() == "yes":
                continueLoop = True  # outerloop continues, more Laptops will be purchaseed
                more = False  # inner loop is terminated

            else:
                read.invalid()
                more = True  # inner loop continues

    print()
    write.purchase_bill(cart)  # function to print and write the bill
    read.purchase()