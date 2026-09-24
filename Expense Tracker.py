track=input("Enter (start/stop): ")
if track.lower()=='start':
    print("Welcome to Expense Tracker💰")
    print("======= MENU =======")
    print("1️⃣  Add Expense")
    print("2️⃣  View All Expenses")
    print("3️⃣  View Total Spendings")
    print("4️⃣  Exit")
    print("====================")
    l=[]
    di={}
    while True:
        choice=int(input("Enter your choice(1-4): "))
        if (choice==1):
            date=input('Enter date(DD-MM-YYYY): ')
            c=input("Enter category (Food 🍕 ,Travel ✈️ ,Shopping 👗 ,etc): ")
            des=input("Enter  short description: ")
            a=int(input("Enter amount(₹):"))
            di[des]=a
            l.append(a)
        elif (choice==2):
            print(f"Your listed expenses with description: {di}")

        elif(choice==3):
            print("🪙 Total spending is",sum(l))

        else:
            break
print("Exited successfully 🎉")





