# Hotel Management System
import csv
# Define global variables
hotel_fields = ['ID', 'Name', 'Age','Address','Country', 'Email', 'Phone','Checkin date','Checkout date','Room number','Roomrent','Resturent bill','Laundry bill','Gaming bill','Total bill']
hotel_database = 'hotelrecord.csv'
def add_Customer():
    print("-------------------------")
    print("Add Customer Information")
    print("-------------------------")
    global hotel_fields
    global hotel_database
Customer_data = []
for i in range(9):
    value = input("Enter " + hotel_fields[i] + ": ")
    Customer_data.append(value)
print ("\n ***** We have The Following Rooms For You *****")
print (" 1. Ultra Royal -----> 10000 Rs.")
print (" 2. Royal -----> 5000 Rs. ")
print (" 3. Elite -----> 3500 Rs. ")
print (" 4. Budget -----> 2500 USD \n")
roomchoice=int(input("Enter Your Choice Please->"))
noofdays=int(input("For How Many Nights Did You Stay:"))
roomno=int(input("Enter Customer Room No : "))
Customer_data.append(roomno)
if roomchoice==1:
    roomrent = noofdays * 10000
    print("\nUltra Royal Room Rent : ",roomrent)
elif roomchoice==2:
    roomrent = noofdays * 5000
    print("\nRoyal Room Rent : ",roomrent)
elif roomchoice==3:
    roomrent = noofdays * 3500
    print("\nElite Royal Room Rent : ",roomrent)
elif roomchoice==4:
    roomrent = noofdays * 2500
    print("\nBudget Room Rent : ",roomrent)
else:
    print("Sorry ,May Be You Are Giving Me Wrong Input, PleaseTry Again !!! ")
    return
dt=[0,0,0,roomrent]
Customer_data.append(roomrent)
Customer_data=Customer_data+dt
with open(hotel_database, "a", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows([Customer_data])
    
print("\nData saved successfully")
input("\nPress any key to continue")
return

def restaurentbill():
    ID=int(input("Enter your ID:"))
    print("\n*****RESTAURANT MENU*****\n")
    print("""1.water----->Rs20 \n2.tea----->Rs10 \n3.breakfast combo--->Rs90 \n4.lunch---->Rs110 \n5.dinner--->Rs150 \n6.Exit\n""")
    choice=int(input("Enter your choice:"))
    quantity=int(input("Enter the quantity:"))
    if (choice==1):
        rtbill = quantity * 20
    elif (choice==2):
        rtbill = quantity * 10
    elif (choice==3):
        rtbill = quantity * 90
    elif (choice==4):
        rtbill = quantity * 110
    elif (choice==5):
        rtbill = quantity * 150
    elif (choice==6):
        return
    else: 
        print("Invalid option")
        return
    print("Total Food Cost=Rs",rtbill,"\n")
    with open(hotel_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        data =[]
        for i in reader:
            if len(i) > 1:
                if i[0]==str(ID):
                    i[11] = eval(i[11]) + rtbill
                    i[14] = eval(i[14]) + rtbill
                    data.append(i)
                else:
                    data.append(i)
    with open(hotel_database, "w", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(data)
    input('\nPress any key to continue')
    return

def gamingbill():
    ID=int(input("Enter your ID:"))
    print ("\n******GAME MENU*******\n")
    print("""1. Table Tennis -----> 150 Rs./HR \n2. Bowling -----> 100 Rs./HR \n3. Snooker -----> 250 Rs./HR \n4. VR World Gaming -----> 400 Rs./HR \n5. Video Games -----> 300 Rs./HR \n6.Swimming Pool Games -----> 350 Rs./HR \n7. Exit\n""")
    game=int(input("Enter What Game You Want To Play : "))
    hour=int(input("Enter No Of Hours You Want To Play : "))
    print("\n\n*************************************************\n")
    if game==1:
        print("YOU HAVE SELECTED TO PLAY : Table Tennis")
        gamingbill = hour * 150
    elif game==2:
        print("YOU HAVE SELECTED TO PLAY : Bowling")
        gamingbill = hour * 100
    elif game==3:
        print("YOU HAVE SELECTED TO PLAY : Snooker")
        gamingbill = hour * 250
    elif game==4:
        print("YOU HAVE SELECTED TO PLAY : VR World Gaming")
        gamingbill = hour * 400
    elif game==5:
        print("YOU HAVE SELECTED TO PLAY : Video Games")
        gamingbill = hour * 300
    elif game ==6:
        print("YOU HAVE SELECTED TO PLAY : Swimming Pool Games")
    elif game ==7:
        return
    else:
        print('Invalid Input')
        return
    print ("Your Total Gaming Bill=Rs",gamingbill,"\n")
    with open(hotel_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        data =[]
        for i in reader:
            if len(i) > 1:
                if i[0] == str(ID):
                    i[13] = eval(i[13]) + gamingbill
                    i[14] = eval(i[14]) + gamingbill
                    data.append(i)
                else:
                    data.append(i)
    with open(hotel_database, "w", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(data)
input('\nPress any key to continue')
return

def laundrybill():
    ID = input('Enter Customer ID : ')
    print ("\n******LAUNDRY MENU*******\n")
    print ("1.Shorts----->Rs3 \n2.Trousers----->Rs4 \n3.Shirt--->Rs5 \n4.Jeans---->Rs6 \n5.Girlsuit--->Rs8 \n6.Exit\n")
    laundary=int(input("Enter your choice:"))
    quantity=int(input("Enter the quantity:"))
    if (laundary==1):
        launbill = laundary * quantity
    elif (laundary==2):
        launbill = laundary * quantity
    elif (laundary==3):
        launbill = laundary *quantity
    elif (laundary==4):
        launbill = laundary *quantity
    elif(laundary==5):
        launbill = laundary *quantity
    elif (laundary==6):
        return
    else:
        print ("Invalid option")
        return
    print ("Your Total Laundry Bill=Rs",launbill,"\n")
    with open(hotel_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        data =[]
        for i in reader:
            if len(i) > 1:
                if i[0] == str(ID):
                    i[12] = eval(i[12]) + launbill
                    i[14] = eval(i[14]) + launbill
                    data.append(i)
                else:
                    data.append(i)
    with open(hotel_database, "w", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(data)
input('\nPress any key to continue')
return

def search():
    Name = input('Enter Customer Name You Want To Search: ')
    with open(hotel_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        count = 0
        data =[]
        for i in reader:
            if len(i) > 1:
                if i[1].lower() == Name.lower():
                    print(i[0:7])
                    count = count + 1
        if count == 0:
            print('No Customer Data Found!')
            input('\nPress any key to continue')
        
def totalbill():
    global hotel_database
    global hotel_fields
    ID = input('Enter Customer ID : ')
    print ("\n******HOTEL BILL******")
    with open('hotelrecord.csv', "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        data =[]
        for i in reader:
            if len(i) > 1:
                if i[0] == str(ID):
                    for j in range(0,15):
                        print('\nCustomer',hotel_fields[j],' :',i[j])
    input('\nPress any key to continue')
    return
while(True):
    print("""1--->Enter Customer Details
2--->Calculate Restaurant Bill
3--->Calculate Laundry Bill
4--->Calculate Game Bill
5--->Search Customer
6--->GENERATE TOTAL BILL AMOUNT
7--->EXIT """)
    choice = int(input("Enter Your Choice : "))
    if choice == 1:
        add_Customer()
    elif choice ==2:
        restaurentbill()
    elif choice == 3:
        laundrybill()
    elif choice ==4:
        gamingbill()
    elif choice ==5:
        search()
    elif choice ==6:
        totalbill()
    elif choice ==7:
        print("-------------------------------")
        print(" Thank you for using our system")
        print("-------------------------------")
        break
