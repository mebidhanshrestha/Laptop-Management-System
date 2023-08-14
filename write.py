import read
def read_file():
    """ This function fetches data from the file """
    file = open("laptop_details.txt", "r")
    data = file.readlines()
    file.close()
    return data


# This function creates a dictionary
def dictionary(file_contents):
    """
        Function converts file's content into dictionary
        Takes content of a txt file as parameter.
        Returns a dictionary with integer keys starting from 1.
    """
    data = {}
    for index in range(len(file_contents)):
        data[index + 1] = file_contents[index].replace("\n", "").split(",")
    return data


def print_laptop(mainData):
    """
        This function shows the list of the laptop by reading the file
        Takes contents of the text file and the dictionary created as a parameter
    """
    print("-----------------------------------------------------------------------------------\n")
    print("ID", "\t", "Laptop Name", "\t", "Brand", "\t", "Price", "\t", "Quantity", "\t", "CPU", "\t\t", "Graphics")
    print("------------------------------------------------------------------------------------\n")
    for key, value in mainData.items():  # Iterates over keys and values of mainData dictionary
        print(key, "\t", value[0], "\t", value[1], "\t", value[2], "\t", value[3], "\t""\t", value[4], "\t", value[5])

    print("\n----------------------------------------------------------------------------------\n")


def write_file(mainData):
    """
        This function writes in the selected text file.
        The quantity of the laptop is reduced if it is called in the sell file,
        and it is increased init is called in the return method in the text file.
    """
    file = open("laptop_details.txt", "w")
    for value in mainData.values():
        write_data = str(value[0]) + "," + str(value[1]) + "," + str(value[2]) + "," + str(value[3]) + "," + str(
            value[4]) + "," + str(value[5]) + "\n"
        file.write(write_data)
    file.close()


def date_time():
    """ This function is for updating date and time in the bill """
    import datetime

    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute

    date = (str(year) + "-" + str(month) + "-" + str(day) + " " + str(hour) + ":" + str(minute))
    return date


def date_t():
    import datetime

    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day

    date_ = (str(year) + "-" + str(month) + "-" + str(day))
    return date_

def sell_bill(cart):
    """
        This function prints and writes the bill of the laptops that have been sold.
        Takes the list 'cart' as a parameter.
    """

    file_contents = read_file()
    mainData = dictionary(file_contents)

    alpha = False
    while alpha == False:
        name = input("Please enter your name: ")
        if name.isalpha():
            alpha = True
        else:
            read.invalid()

    int_contact = False
    while int_contact == False:
        try:
            contact = int(input(
                "Please enter your contact number: "))  # here the string value of the contact is changed into integer datatype
            int_contact = True  # loop is terminated
        except:
            read.invalid()  # loop continues as an exception is thrown

    # printing of bill starts here
    print()
    print("\n--------------- INVOICE ---------------\n")
    print("\n" + "Name: " + name)
    print("Phone no.: " + str(contact))
    date = date_time()
    print("Date: " + str(date) + "\n")

    print("--------------------------------------------------------------------------------------------------")
    print("ID", "\t", "Laptop Name", "\t", "Brand", "\t", "Price", "\t", "Quantity", "\t", "CPU", "\t\t", "Graphics")
    print("------------------------------------------------------------------------------------------------\n")

    total = 0
    for index in range(len(cart)):
        laptop_id = int(cart[index][0])
        laptop_quantity = int(cart[index][1])
        laptop_name = mainData[laptop_id][0]
        laptop_brand = mainData[laptop_id][1]
        laptop_price = int(mainData[laptop_id][2].replace("$", "")) * laptop_quantity
        laptop_CPU = (mainData[laptop_id][4])
        laptop_Graphics = (mainData[laptop_id][5])
        grand_total = laptop_price * laptop_quantity
        total += grand_total

        print(str(index + 1), "\t", laptop_name, "\t", laptop_brand, "\t", str(laptop_price), "\t",
              str(laptop_quantity), "\t""\t", laptop_CPU, "\t", laptop_Graphics)
        print("\n")
    total_with_shipping_cost=total+100
    print("Grand Total: " + str(total)+ "\n")
    print("Grand Total with shipping cost: ", str(total_with_shipping_cost)+ "\n")
    # bill ends here

    # writing the bill starts here
    file = open(name + "_" + str(date_t()) + ".txt", "w")  # a text file with the name of the user is created

    file.write("\n---------------------INVOICE---------------------\n")
    file.write("\n" + "Name: " + name + "\n")
    file.write("Phone no.: " + str(contact) + "\n")
    date = date_time()
    file.write("Date: " + str(date) + "\n\n")

    file.write("-------------------------------------------------------------")
    file.write("\nID\tLaptop Name\tBrand\tPrice\tQuantity\tCPU\tGraphics\n")
    file.write("-------------------------------------------------------------\n\n")

    total = 0
    for index in range(len(cart)):
        laptop_id = int(cart[index][0])
        laptop_quantity = int(cart[index][1])
        laptop_name = mainData[laptop_id][0]
        laptop_brand = mainData[laptop_id][1]
        laptop_price = int(mainData[laptop_id][2].replace("$", "")) * laptop_quantity
        laptop_cpu = (mainData[laptop_id][4])
        laptop_graphics = (mainData[laptop_id][5])
        grand_total = laptop_price * laptop_quantity
        total += grand_total
        
        file.write(str(index + 1) + "\t" + laptop_name + "\t" + laptop_brand + "\t" + str(laptop_price) + "\t" + str(
            laptop_quantity) + "\t" + laptop_cpu + "\t" + laptop_graphics)
        file.write("\n\n")
    total_with_shipping_cost=total+100
    file.write("-------------------------------------------------------------\n\n")

    file.write("Grand Total: " + str(total)+ "\n")
    file.write("Grand Total with shipping cost:  " + str(total_with_shipping_cost)+ "\n")
    file.write("\n\n-------------------------------------------------------------")
    file.write("\n        Thank you! The laptos have been purchsed.          \n")
    file.write("-------------------------------------------------------------")

    file.close()
    # the text file ends here


def purchase_bill(cart):
    """
        This function prints and writes the bill of the sells that have been purchase for store.
        Takes the list 'cart' as a parameter.
    """

    file_contents = read_file()
    mainData = dictionary(file_contents)

    alpha = False
    while alpha == False:  # this loop checks whether the name is in alphabetic form or not
        name = input("Please enter your name: ")
        if name.isalpha():  # if the name is found alphabetic then the loop is terminated
            alpha = True
        else:
            read.invalid()

    int_contact = False
    while int_contact == False:
        try:
            contact = int(input("Please enter your contact number: "))
            int_contact = True
        except:
            read.invalid()

    # bill printing starts here
    print()
    print("\n--------------------------INVOICE------------------------------")
    print("\n" + "Name: " + name)
    print("Phone no.: " + str(contact))
    date = date_time()
    print("Date: " + str(date))
    print("------------------------------------------------------------------------------------")
    print("ID", "\t", "Laptop Name", "\t", "Brand", "\t", "Price", "\t", "Quantity", "\t", "CPU", "\t""\t", "Graphics")
    print("-----------------------------------------------------------------------------------\n")

    total = 0
    for index in range(len(cart)):
        laptop_id = int(cart[index][0])
        laptop_quantity = int(cart[index][1])
        laptop_name = mainData[laptop_id][0]
        laptop_brand = mainData[laptop_id][1]
        laptop_price = int(mainData[laptop_id][2].replace("$", "")) * laptop_quantity
        laptop_cpu = (mainData[laptop_id][4])
        laptop_graphics = (mainData[laptop_id][5])
        grand_total = laptop_price * laptop_quantity
        total += grand_total
        print(str(index + 1), "\t", laptop_name, "\t", laptop_brand, "\t", str(laptop_price), "\t",
              str(laptop_quantity), "\t""\t", laptop_cpu, "\t", laptop_graphics)
        print("\n")
    vat_total=(total+(total*13/100))
    print("Total purchase = " + str(total) + "\n")
    print("Total purchase with 13% vat is " + str(vat_total) + "\n")
    # bill printing ends here

    # bill generation(writing bill) starts here
    file = open(name + "_" + str(date_t()) + ".txt", "w")  # a text file with the name of the user is created

    file.write("\n------------------------INVOICE------------------------\n")
    file.write("\n" + "Name: " + name + "\n")
    file.write("Phone no.: " + str(contact) + "\n")
    date = date_time()
    file.write("Date: " + str(date) + "\n\n")

    file.write("-------------------------------------------------------------")
    file.write("\nID\tLaptop Name\tBrand\tPrice\tQuantity\tCPU\tGraphics\n")
    file.write("-------------------------------------------------------------\n\n")

    total = 0
    for index in range(len(cart)):
        laptop_id = int(cart[index][0])
        laptop_quantity = int(cart[index][1])
        laptop_name = mainData[laptop_id][0]
        laptop_brand = mainData[laptop_id][1]
        laptop_price = int(mainData[laptop_id][2].replace("$", "")) * laptop_quantity
        laptop_cpu = (mainData[laptop_id][4])
        laptop_graphics = (mainData[laptop_id][5])
        grand_total = laptop_price * laptop_quantity
        total += grand_total
        file.write(str(index + 1) + "\t" + laptop_name + "\t" + laptop_brand + "\t" + str(laptop_price) + "\t" + str(
            laptop_quantity) + "\t" + laptop_cpu + "\t" + laptop_graphics)
        file.write("\n\n")
    vat_total=(total+(total*13/100))
    file.write("-------------------------------------------------------------\n\n")
    file.write("Total purchase: " + str(total)+ "\n")
    file.write("Total purchase  with 13% vat is " + str(vat_total)+ "\n")
    file.write("\n\n-------------------------------------------------------------")
    file.write("\n        Thank you! The purchase have been great.          \n")
    file.write("----------------------------------------------------------------")

    file.close()
    # bill generation ends here
