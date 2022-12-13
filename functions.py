#this file contains all the functions
import datetime #importing datetime module

def welcome():
    '''function for welcome message'''
    print("\n\n",27*"+"+" --\\\U0001f600 /-- "+ 27*"+")
    print(" ++++++"+"\t\tW3lcom3 To Bik3 M@n@g3m3nt Syst3m"+"\t   ++++++")
    print("",64*"+","\n")

def open_text_file():
    '''function for opening text file'''
    file = open("bike.txt","r")
    return file

def show_bikes():
    '''function for displaying bikes'''
    print("\n\n","-" * 64 + "\n| Bike_ID  | Bike_Name  | Company_Name \t| Color |Quntity| Price |" + "\n" + "-" * 65)
    file = open_text_file()
    id = 1
    for line in file:
        print("|  " , id ,"\t   |" + line.replace(",","\t|"))
        id +=1
        print("-" * 64)
    print("\n\n")
    file.close()

def add_2d_list():
    '''function for 2d list'''
    file = open_text_file()
    matrix = []
    for i in file:
        i = i.replace("\n","")
        matrix.append(i.split(","))
    file.close()
    return(matrix)

def user_operation():
    '''function to ask user for differen operation'''
    print("\n\n",64 * "+")
    print(12 * "+","  Enter 1 to purchase the bike  ","+" * 18)
    print(12 * "+","  Enter 2 to add stock          ","+" * 18)
    print(12 * "+","  Enter 3 to exit the System    ","+" * 18)
    print(64 * "+")
    print("\n\n")

def main_Code():
    '''function for checking user input'''
    welcome()
    show_bikes()
    print(add_2d_list())
    user_operation()
    loop = True
    while loop:
        try:
            user_input = int(input("Enter the number : "))
            if user_input == 1:
                bike_id = validating_bike_id()
                customer_details = customer_detail()
                show_bikes()
                quantity = qty_validation(bike_id)
                sell(bike_id,quantity)
                total_price = price(bike_id,quantity)
                report(bike_id,quantity,total_price,customer_details)
            elif user_input == 2: 
                show_bikes()
                bike_id1 = validating_bike_id1()
                company_details = company_detail()
                show_bikes()
                quantity1 = qty_validation1(bike_id1)
                increasing_quantity(bike_id1,quantity1)
                total_price1 = price1(bike_id1,quantity1)
                report1(bike_id1,quantity1,total_price1,company_details)
            elif user_input == 3:
                exit_system()
                loop = False
            else: 
                invalid_input()
        except ValueError:
            print("\n","*" * 64)
            print("\n","*" * 16+"  Supports Integer Value on!y  "+ "*" * 16,"\n")
            print("*" * 64,"\n")

def validating_bike_id():
    '''function for bike_id validation'''
    loop = True
    while loop:
        try:
            print("\n")
            valid_id = int(input("Enter the id of bike you want to buy: "))
            print("\n")
            while valid_id <= 0 or valid_id > len(add_2d_list()):
                print(64 * "+","\n",12 * "+","  Please provide a valid Bike_ID     ","+" * 12,"\n","+" * 64)
                print("\n")
                show_bikes()
                print("\n")
                valid_id = int(input("Enter the id of bike you want to buy: "))
                print("\n")
            return valid_id
        except ValueError:
            print("\n","*" * 64)
            print("\n","*" * 16+"  Supports Integer Value on!y  "+ "*" * 16,"\n")
            print("*" * 64,"\n")

def customer_detail():
    '''details of customer'''
    name = input("Enter your full name : ")
    address = input("Enter your current address : ")
    contact = input("Enter your contact detail : ")
    email = input("Enter your email : ")
    return name,address,contact,email

def qty_validation(bike_id):
    '''function for quantity validation'''
    loop = True
    while loop:
        try:
            bike_collection = add_2d_list()
            user_qty = int(input("Enter the quantity you want to purchase: "))
            while user_qty <= 0 or user_qty > int(bike_collection[bike_id - 1][3]):
                print("\n")
                print(64 * "+","\n",12 * "+","  Please provide a valid quantity    ","+" * 12,"\n","+" * 64)
                print("\n")
                show_bikes()
                user_qty = int(input("Enter the quantity you want to purchase: "))
                print("\n")
            return user_qty
        except ValueError:
            print("\n","*" * 64)
            print("\n","*" * 16+"  Supports Integer Value on!y  "+ "*" * 16,"\n")
            print("*" * 64,"\n")

def update_qty(bike_collection):
    '''function for updating the quantity value of specific bike'''
    file = open("bike.txt","w")
    for i in bike_collection:
        file.write(str(i[0]) + "," + str(i[1]) + "," + str(i[2]) + "," + str(i[3]) + "," + str(i[4]) + "\n")
    file.close()
    show_bikes()

def sell(bike_id,quantity):
    '''function for subtracting the quantity from the stock'''
    bike_collection = add_2d_list()
    bike_collection[bike_id -1][3] = int(bike_collection[bike_id - 1][3]) - quantity
    update_qty(bike_collection)

def price(bike_id,quantity):
    '''function for bike price'''
    bike_collection = add_2d_list()
    total_cost = int(bike_collection[bike_id - 1][4].replace("$","")) * int(quantity)
    print("\n",64 * "+","\n","\tThe price of ",quantity,"quantity naming bike_id",bike_id,"is ","$",total_cost,"\n","+" * 64)
    print("\n")
    return total_cost

#Purchase report
def report(bike_id,quantity,total_price,customer_details):
    '''function for writing purchase detail in unique file'''
    currentDateTime = str(datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S"))
    #getting values from customer_detail function
    name,address,contact,email = customer_details

    #purchasing report writing in file
    bike_collection = add_2d_list()
    bike_name = str(bike_collection[bike_id-1][0])
    bike_company = str(bike_collection[bike_id-1][1])
    bike_color = str(bike_collection[bike_id-1][2])
    bike_quantity = str(quantity)
    bike_price =str(total_price)
    
    report_file = open(name+"_"+contact+".txt","w")
    report_file.write("*" * 140 + "\n")
    report_file.write("\t\t\t\t\t\t\tPurchase report"+"\n\n")
    report_file.write("*" * 140)
    report_file.write("\n"+ "-" * 140+"\n")
    report_file.write("Bike_id |Customer_name  | Bike_Name  | Company_Name | Color | Quntity| Price |    Date and Time\t|   Address   |   Contact   | E-Mail " + "\n")
    report_file.write("-" * 140 + "\n")
    report_file.write(str(bike_id)+"\t   "+name+"\t  "+bike_name+"\t "+bike_company+"     "+bike_color+"\t  "+bike_quantity+"\t"+bike_price+"   "+currentDateTime+"  "
                      +address+"    "+contact+"\t  "+email+"\n")
    report_file.write("-" * 140+"\n")
    
    report_file.close()
    
    #display purchase report
    display_file = open(name+"_"+contact+".txt","r")
    for output in display_file:
        print(output)
    purchase_other_bikes(bike_id,customer_details)
    user_operation()

#writing in existing file
def reports(bike_id,quantity,total_price,customer_details):
    '''function for writing purchase detail in existing file'''
    currentDateTime = str(datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S"))
    #getting values from customer_detail function
    name,address,contact,email = customer_details

    #purchasing report writing in file
    bike_collection = add_2d_list()
    bike_name = str(bike_collection[bike_id-1][0])
    bike_company = str(bike_collection[bike_id-1][1])
    bike_color = str(bike_collection[bike_id-1][2])
    bike_quantity = str(quantity) 
    bike_price =str(total_price)
    
    report_file = open(name+"_"+contact+".txt","a")
    report_file.write(str(bike_id)+"\t   "+name+"\t  "+bike_name+"\t "+bike_company+"     "+bike_color+"\t  "+bike_quantity+"\t"+bike_price+"   "+currentDateTime+"  "
                      +address+"    "+contact+"\t  "+email+"\n")
    report_file.write("-" * 140+"\n")
    report_file.close()
    
#purchase more then one bikes
def purchase_other_bikes(bike_id,customer_details):
    '''function for adding similar or different bikes by same customer'''
    loop = True
    while loop:
        try:
            print("*" * 40)
            print("If You want to add more, then use: " + "Y")
            print("If You don't want to add, then use: " + "N")
            print("*" * 40,"\n")
            user_input = input("Do you want to purchase another bike: "+"\n").upper()
            if user_input == "Y":
                bike_id = validating_bike_id()
                show_bikes()
                quantity = qty_validation(bike_id)
                sell(bike_id,quantity)
                total_price = price(bike_id,quantity)
                reports(bike_id,quantity,total_price,customer_details)
            else:
                user_input == "N"
                exit_system()
                loop = False
        except ValueError:
            print("\n","*" * 64)
            print("\n","*" * 16+"  supports Y/N only!!  "+ "*" * 16,"\n")
            print("*" * 64,"\n")


def validating_bike_id1():
    '''function for bike_id validation'''
    loop = True
    while loop:
        try:
            print("\n")
            valid_id = int(input("Enter the id of bike you want to buy: "))
            print("\n")
            while valid_id <= 0 or valid_id > len(add_2d_list()):
                print(64 * "+","\n",12 * "+","  Please provide a valid Bike_ID     ","+" * 12,"\n","+" * 64)
                print("\n")
                show_bikes()
                print("\n")
                valid_id = int(input("Enter the id of bike you want to buy: "))
                print("\n")
            return valid_id
        except ValueError:
            print("\n","*" * 64)
            print("\n","*" * 16+"  Supports Integer Value on!y  "+ "*" * 16,"\n")
            print("*" * 64,"\n")
            
def company_detail():
    '''function for the detail of the company'''
    shipping_company_name = input("Enter the shipping company name: ")
    shipping_cost = input("Enter the shipping cost of the bikes: ")
    return shipping_company_name,shipping_cost

def qty_validation1(bike_id1):
    '''function for quantity validation'''
    loop = True
    while loop:
        try:
            bike_collection = add_2d_list()
            user_qty = int(input("Enter the quantity you want to add: "))
            while user_qty <= 0:
                print("\n")
                print(64 * "+","\n",12 * "+","  Please provide a valid quantity    ","+" * 12,"\n","+" * 64)
                print("\n")
                show_bikes()
                user_qty = int(input("Enter the quantity you want to add: "))
                print("\n")
            return user_qty
        except ValueError:
            print("\n","*" * 64)
            print("\n","*" * 16+"  Supports Integer Value on!y  "+ "*" * 16,"\n")
            print("*" * 64,"\n")

def increasing_quantity(bike_id1,quantity1):
    '''function for adding the quantity for already exist bike_id'''
    bike_collection = add_2d_list()
    bike_collection[bike_id1 -1][3] = int(bike_collection[bike_id1 - 1][3]) + quantity1
    update_qty(bike_collection)

def price1(bike_id1,quantity1):
    '''function for bike price'''
    bike_collection = add_2d_list()
    total_cost = int(bike_collection[bike_id1 - 1][4].replace("$","")) * int(quantity1)
    print("\n",64 * "+","\n","\tThe price of ",quantity1,"quantity naming bike_id",bike_id1,"is ","$",total_cost,"\n","+" * 64)
    print("\n")
    return total_cost

#add stock report
def report1(bike_id1,quantity1,total_price1,company_detail):
    '''function for writing add stock detail in unique file'''
    currentDateTime = str(datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S"))
    #getting values from company_detail function
    shipping_company_name,shipping_cost = company_detail

    #adding stock report writing in file
    bike_collection = add_2d_list()
    c = 1
    bike_name = str(bike_collection[bike_id1-1][0])
    bike_company = str(bike_collection[bike_id1-1][1])
    bike_color = str(bike_collection[bike_id1-1][2])
    bike_quantity = str(quantity1)
    bike_price =str(total_price1)
    
    report_file = open(shipping_company_name+"_"+shipping_cost+".txt","w")
    report_file.write("*" * 118 + "\n")
    report_file.write("\t\t\t\t\t\t\tAdding stock report"+"\n\n")
    report_file.write("*" * 118)
    report_file.write("\n"+ "-" * 118+"\n")
    report_file.write("S.N |shipping_Company  | Bike_Name  | Company_Name | Color | Quntity| Price |    Date and Time\t    | shipping_cost" + "\n")
    report_file.write("-" * 118 + "\n")
    report_file.write(str(c)+"\t"+shipping_company_name+"\t\t "+bike_name+"\t       "+bike_company+"\t     "+bike_color+"     "+bike_quantity+"      "+bike_price+"\t"
                      +currentDateTime+"\t"+shipping_cost+"\n")
    report_file.write("-" * 118+"\n")
    report_file.close()
    
    #display adding stock report
    display_file = open(shipping_company_name+"_"+shipping_cost+".txt","r")
    for output in display_file:
        print(output)
    user_operation()
    
def exit_system():
    '''function for existing the system'''
    print("\n\n")
    print(64 * "+","\n",16 * "+","Th@nk$ for using our syst3m  ","+" * 16,"\n","+" * 64)
    print("\n\n")

def invalid_input():
    '''function for invalid input'''
    print("\n\n")
    print(64 * "+","\n",16 * "+","Please Enter Valid number        ","+" * 12,"\n",16 * "+","Please! enter 1,2,3 options      ","+" * 12
          ,"\n","+" * 64)
    print("\n\n")



