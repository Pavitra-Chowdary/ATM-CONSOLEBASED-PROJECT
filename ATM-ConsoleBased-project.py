print("--------------------------------")
print("Welcome to ATM")
print("----------------------------")
print()

accounts = {
    1440: ["Pavitra","29-08-2003",48000,2429],
    1441: ["Anjineyulu","10-08-1994",20000,1008],
    1442: ["Aasritha","03-01-2004",5000,None],
    1443: ["Adhithi","14-03-2004",25000,1403],
    1444: ["Lakshmi","07-10-1982",14000, 7010],
    1445: ["Ravindhra","24-07-2000",60000,6789],
    1446: ["Sai Teja","17-12-2004",12000,1712],
    1447: ["Shankar Naidu","05-06-1990",18000,5006]
}

dobm = {1: "January", 2: "Feb", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec"}

while True:
    print("Choose Your Option")
    print("1. Withdrawal")
    print("2. Deposit")
    print("3. Pin Generation")
    print("4. Mini Statement")
    print("5. Reset Pin")
    print("6. Check Balance")
    print("7. Change Mobile Number")
    print("8. View Account Details")
    print("9. Exit")
    option = int(input("Enter Your Option: "))
    print()
    
    if option == 1:
        print("---------------------------------------")
        accno = int(input("Enter Account Number: "))
        if accno not in accounts:
            print("Account Does not Exist!")
        else:
            pin = int(input("Enter Pin: "))
            if accounts[accno][-1] is None:
                print("Generate Pin")
            elif accounts[accno][-1] != pin:
                print("Invalid Pin")
            else:
                amt = int(input("Enter Amount to Withdraw: "))
                if amt > accounts[accno][-2]:
                    print("Insufficient Balance")
                else:
                    print("Withdrawal Successful!")
                    accounts[accno][-2] -= amt
        print("-----------------------------")
    
    elif option == 2:
        print("------------------------------------")
        accno = int(input("Enter Account Number: "))
        if accno not in accounts:
            print("Account does not Exist")
        else:
            amt = int(input("Enter Amount to Deposit: "))
            accounts[accno][-2] += amt
            print("Deposit Successful")
        print("-----------------------------------")
    
    elif option == 3:
        print("-------------------------------------")
        accno = int(input("Enter Account Number: "))
        if accno not in accounts:
            print("Account Does not Exist")
        else:
            if accounts[accno][-1] is None:
                pin = int(input("Enter Pin: "))
                cpin = int(input("Confirm Pin: "))
                if pin != cpin:
                    print("Pin Does not Match")
                else:
                    accounts[accno][-1] = pin
                    print("Pin Generated Successfully")
            else:
                print("Pin Already Exists")
        print("---------------------------------------")
    
    elif option == 4:
        print("---------------------------------------")
        accno = int(input("Enter Account Number: "))
        if accno not in accounts:
            print("Account Does not Exist")
        else:
            pin = int(input("Enter Pin: "))
            if pin != accounts[accno][-1]:
                print("Invalid Pin")
            else:
                print(f"Name: {accounts[accno][0]}")
                print(f"Account Number: {accno}")
                dob = accounts[accno][1].split("-")
                date = dob[0]
                month = dobm[int(dob[1])]
                year = dob[2]
                formatted_dob = f"{date}-{month}-{year}"
                print(f"Date of Birth: {formatted_dob}")
                print(f"Account Balance: {accounts[accno][-2]}")
        print("-----------------------------")
    
    elif option == 5:
        print("-----------------------------------")
        accno = int(input("Enter Account Number: "))
        if accno not in accounts:
            print("Account Does not Exist")
        else:
            pin = int(input("Enter Old Pin: "))
            if pin != accounts[accno][-1]:
                print("Invalid Pin")
            else:
                new_pin = int(input("Enter New Pin: "))
                confirm_pin = int(input("Confirm New Pin: "))
                if new_pin != confirm_pin:
                    print("Pin Does not Match")
                else:
                    accounts[accno][-1] = new_pin
                    print("Pin Reset Successfully")
        print("-----------------------------------------")
    
    elif option == 6:
        accno = int(input("Enter Account Number: "))
        if accno in accounts:
            print(f"Your Account Balance is: {accounts[accno][-2]}")
        else:
            print("Account Does not Exist")
        print("-------------------------------------")
    
    elif option == 7:
        print("------------------------------------")
        accno = int(input("Enter Account Number: "))
        if accno not in accounts:
            print("Account Does not Exist")
        else:
            new_mobile = input("Enter New Mobile Number: ")
            accounts[accno].append(new_mobile)
            print("Mobile Number Updated Successfully")
        print("--------------------------------")
    
    elif option == 8:
        print("-----------------------------------")
        accno = int(input("Enter Account Number: "))
        if accno in accounts:
            print(f"Account Details: {accounts[accno]}")
        else:
            print("Account Does not Exist")
        print("----------------------------------")
    
    elif option == 9:
        print("Thank You Visit Again")
        break
