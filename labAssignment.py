# Lab Professor: Mr. Hesam Akbari
employeeInfor = [["Employee ID", "Employee Name", "Employee Type", "Years Worked", "Total Purchased", "Total Discount", "Employee Discount Number"]]
itemInfor = [["Item Number", "Item Name", "Item Price"],
             ["11526", "Nike Shoes", "120"],
             ["11849", "Trampoline", "180"],
             ["11966", "Mercury Bicycle", "150"],
             ["11334", "Necklace Set", "80"]]
totalPrice = 0

def dashedLine():
    for i in range(0, 1):
        for j in range(0, i + 50):
            print("_", end="_")
    print(" ")


def insertColumn(string):
    string = string[:0] + "| " + string[0:]
    for i in range(0, 1):
        for j in range(0, i + 100):
            string += " "
    if len(string) > 100:
        string = string[:98] + " |" + string[98:]
    return string


def action():
    dashedLine()
    employee = "1 - Create Employee "
    item = "2 - Create Item"
    makePurchase = "3 - Make Purchase"
    summary = "4 - All Employee Summary"
    endProgram = "5 - Exit"
    print(insertColumn(employee))
    print(insertColumn(item))
    print(insertColumn(makePurchase))
    print(insertColumn(summary))
    print(insertColumn(endProgram))
    dashedLine()
    return input("Pick one of the following choices (EX: 1, 2, 3, 4, 5): ")


def main():
    while True:
        choice = action()
        if choice == "1":
            print(employeeInfo(employeeInfor))
        elif choice == "2":
            print(createItem(itemInfor))
        elif choice == "3":
            print(purchasePage(itemInfor, employeeInfor, totalPrice))
        elif choice == "4":
            print(purchaseSummary())
        elif "1" < choice > "5":
            print("\n It must be between 1 and 5")
        elif choice == "5":
            print("Have a nice day!")
            exit()

##Create Employee Information
def employeeInfo(employeeInformation):
    ##Asks for the employee ID
    employeeID = input("Your Employee ID: ")
    while not employeeID.isnumeric() or hasDuplicateID(employeeID, employeeInformation):
        print("The input is invalid, try again! ")
        employeeID = input("Your Employee ID: ")

    ##Asks for the first name of the employee
    employeeFirstName = input("Your First Name Employee: ")
    while not employeeFirstName.isalpha():
        print("The input is invalid! Try Again! ")
        employeeFirstName = input("Your First Name Employee: ")

    ##Asks for the last name of the employee
    employeeLastName = input("Your Last Name Employee: ")
    while not employeeLastName.isalpha():
        print("The input is invalid! Try Again! ")
        employeeLastName = input("Your Last Name Employee: ")

    ##Asks for the type of employee of the worker
    employeeType = input("Type of Employee (hourly or manager): ")
    while not employeeType.lower() == "hourly" and not employeeType.lower() == "manager":
        print("You choices are hourly or manager! Try Again! ")
        employeeType = input("Type of Employee (hourly or manager): ")

    ##Asks for years worked
    yearsWorked = input("# of Years Worked: ")
    while not yearsWorked.isnumeric():
        print("The input is not number! Try Again! ")
        yearsWorked = input("# of Years Worked: ")

    totalPurchase = 0
    totalDiscount = 0
    if int(yearsWorked) / 2 >= 10:
        totalDiscount = 10
    elif int(yearsWorked) / 2 < 10:
        totalDiscount = int(yearsWorked) / 2

    if employeeType.lower() == "manager":
        totalDiscount += 10
    elif employeeType.lower() == "hourly":
        totalDiscount += 2

    ##Asks for employee discount
    discountNumber = input("Employee Discount #: ")
    while not discountNumber.isnumeric() or hasDuplicateDiscount(discountNumber, employeeInformation):
        print("The input is invalid! Try Again! ")
        discountNumber = input("Employee Discount #: ")

    employeeInformation += [
        [employeeID, employeeFirstName + " " + employeeLastName, employeeType, yearsWorked, totalPurchase, str(totalDiscount) + "%", discountNumber]]

    ##Check if the user wants to input another employee
    anotherEmployee = input("Another Employee (yes/no): ")
    while not anotherEmployee.lower() == "yes" and not anotherEmployee.lower() == "no":
        print("Either yes or no")
        anotherEmployee = input("Another Employee (yes/no): ")
    if anotherEmployee.lower() == "yes":
        employeeInfo(employeeInformation)
    elif anotherEmployee.lower() == "no":
        ##Checks if the user wants to keep using it or quit the program
        checkMenu = input("Go to Menu (yes/no)? ")
        while not checkMenu.lower() == "yes" and not checkMenu.lower() == "no":
            print("Either yes or no")
            checkMenu = input("Go to Menu (yes/no)? ")
            if checkMenu.lower() == "yes":
                main()
                return employeeInformation
            elif checkMenu.lower() == "no":
                print("Have a nice day!")
                break
    return employeeInformation

##Check for discount duplicates
def hasDuplicateDiscount(element, array):
    for i in array:
        if element == i[6]:
            return True
    return False

##Check for employee id duplicates
def hasDuplicateID(element, array):
    for i in array:
        if element == i[0]:
            return True
    return False

def createItem(itemInfo):
    ##Asks for the item Number
    itemNumber = input("Can I have the item #: ")
    while not itemNumber.isnumeric() or hasDuplicateID(itemNumber, itemInfo) or len(itemNumber) == 0:
        print("The input is invalid! Try Again!")
        itemNumber = input("Can I have the item #: ")
    ##Asks for the item Name
    itemName = input("Can I have the item name: ")
    while len(itemName) == 0:
        print("This field cannot be empty! Try Again!")
        itemName = input("Can I have the item name: ")
    ##Asks for the item Price
    itemPrice = input("Can I have the price of the item: ")
    while not itemPrice.isnumeric() or len(itemPrice) == 0:
        print("The input is invalid! Try Again!")
        itemPrice = input("Can I have the price of the item: ")

    itemInfo += [[itemNumber, itemName, itemPrice]]

    anotherItem = input("Another Item (yes/no)? ")
    while not anotherItem.lower() == "yes" and not anotherItem.lower() == "no":
        print("Input must be either yes or no")
        anotherItem = input("Another Item (yes/no)? ")
    if anotherItem.lower() == "yes":
        createItem(itemInfo)
    elif anotherItem.lower() == "no":
        ##Checks if the user wants to keep using it or quit the program
        checkMenu = input("Go to Menu (yes/no)? ")
        while not checkMenu.lower() == "yes" and not checkMenu.lower() == "no":
            print("Either yes or no")
            checkMenu = input("Go to Menu (yes/no)? ")
        if checkMenu.lower() == "yes":
            main()
            return itemInfo
        elif checkMenu.lower() == "no":
            print("Have a nice day!")
            exit()
    return itemInfo


def purchasePage(itemInfo, employeeInfo, totalPrice):
    tempPrice = 0
    for line in itemInfo:
        print("{: <20}| {: <20}| {: <20}".format(*line))

    employeeDiscountNumber = input("Employee Discount Number: ")
    while not employeeDiscountNumber.isnumeric() or not hasDuplicateDiscount(employeeDiscountNumber, employeeInfo):
        print("Employee discount not found! Try Again!")
        employeeDiscountNumber = input("Employee Discount #: ")

    itemNumber = input("Item Number: ")
    while not itemNumber.isnumeric() or not hasDuplicateID(itemNumber, itemInfo):
        print("Item number not found in the list. Try Again!")
        itemNumber = input("Item Number: ")

    for i in itemInfo:
        for j in employeeInfo:
            if i[0] == itemNumber and j[6] == employeeDiscountNumber:
                totalPrice += int(i[2])
                discount = ((100 - int(j[5]))/100)
                difference = totalPrice - (totalPrice*discount)
                print("total = " + str(totalPrice))
                print("difference = " + str(difference))
                if difference > 200:
                    print("You have already exceeded the discount limit of $200 discount")
                    totalPrice = totalPrice - int(i[2])
                    j[4] = totalPrice * discount
    newPurchase = input("Another Purchase (yes/no)? ")
    while not newPurchase.lower() == "yes" and not newPurchase.lower() == "no":
        print("Either yes or no")
        newPurchase = input("Another Purchase (yes/no)? ")
    if newPurchase.lower() == "yes":
        purchasePage(itemInfo, employeeInfo, totalPrice)
    elif newPurchase.lower() == "no":
        j[4] = totalPrice * discount
        totalPrice = 0
        for i in employeeInfor:
            print("{: <15}| {: <15}| {: <15}| {: <15}| {: <15}| {: <15}| {: <15}".format(*i))

    checkMenu = input("Go to Menu (yes/no)? ")
    while not checkMenu.lower() == "yes" and not checkMenu.lower() == "no":
        print("Either yes or no")
        checkMenu = input("Go to Menu (yes/no)? ")
    if checkMenu.lower() == "yes":
        main()
        return itemInfo, employeeInfo, totalPrice, tempPrice
    elif checkMenu.lower() == "no":
        print("Have a nice day!")
        exit()


def purchaseSummary():
    for i in employeeInfor:
        print("{: <15}| {: <15}| {: <15}| {: <15}| {: <15}| {: <15}| {: <15}".format(*i))

    checkMenu = input("Go to Menu (yes/no)? ")
    while not checkMenu.lower() == "yes" and not checkMenu.lower() == "no":
        print("Either yes or no")
        checkMenu = input("Go to Menu (yes/no)? ")
    if checkMenu.lower() == "yes":
        main()
    elif checkMenu.lower() == "no":
        print("Have a nice day!")
        exit()


if __name__ == '__main__':
    main()
