
class Customer:
    def __init__(self):
        self.cid = ""
        self.cname = ""
        self.acc_no = ""
        self.balance = 0.0
        self.credit_card = []

    def transfer_funds(self, beneficiary_cust_object, amount):
        if amount <= 0:
            print("Enter a positive amount.")
        elif amount > self.balance:
            print("Not enough funds.")
        else:
            self.balance -= amount
            beneficiary_cust_object.balance += amount
            print("Transfer successful.")
            print("Your new balance:", self.balance)
            print("Beneficiary new balance:",
                  beneficiary_cust_object.balance)

    def assign_card(self, card_object):
        self.credit_card.append(card_object)
        print("Card assigned successfully.")

    def display_customer(self):
        print("\nCUSTOMER INFORMATION")
        print("Customer ID:", self.cid)
        print("Customer name:", self.cname)
        print("Account number:", self.acc_no)
        print("Balance:", self.balance)
        print("Credit cards:")

        if len(self.credit_card) == 0:
            print("No cards assigned.")
        else:
            for card in self.credit_card:
                print(card.card_no)


class Card:
    def __init__(self):
        self.card_no = ""
        self.cvv = ""
        self.expiry_date = ""
        self.balance = 0.0

    def display_card(self):
        print("\nCARD INFORMATION")
        print("Card number:", self.card_no)
        print("CVV:", self.cvv)
        print("Expiry date:", self.expiry_date)
        print("Balance:", self.balance)


myCustomersList = []
myCardsList = []

while True:
    print("\nMAIN MENU")
    print("1. Create Customer Objects")
    print("2. Create Card Objects")
    print("3. Transfer Funds Between Customer Objects")
    print("4. Assign Card Objects to Customer Objects")
    print("5. Display Customer Info")
    print("6. Display Card Info")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        cid = int(input("Enter customer ID: "))

        found = False
        for cus in myCustomersList:
            if cus.cid == cid:
                found = True

        if found:
            print("Customer ID already exists.")
        else:
            cname = input("Enter customer name: ")
            acc_no = input("Enter account number: ")
            balance = float(input("Enter initial balance: "))

            if balance < 0:
                print("Balance cannot be negative.")
            else:
                cus = Customer()
                cus.cid = cid
                cus.cname = cname
                cus.acc_no = acc_no
                cus.balance = balance

                myCustomersList.append(cus)
                print("Customer created successfully.")

    elif choice == 2:
        card_no = input("Enter card number: ")

        found = False
        for card in myCardsList:
            if card.card_no == card_no:
                found = True

        if found:
            print("Card number already exists.")
        else:
            cvv = input("Enter CVV: ")
            expiry_date = input("Enter expiry date (MM/YY): ")
            balance = float(input("Enter card balance: "))

            if balance < 0:
                print("Balance cannot be negative.")
            else:
                crd = Card()
                crd.card_no = card_no
                crd.cvv = cvv
                crd.expiry_date = expiry_date
                crd.balance = balance

                myCardsList.append(crd)
                print("Card created successfully.")

    elif choice == 3:
        if len(myCustomersList) < 2:
            print("Create at least 2 customers first.")
        else:
            for cus in myCustomersList:
                print("ID:", cus.cid, "| Name:", cus.cname,
                      "| Balance:", cus.balance)

            sender_id = int(input("Enter sender customer ID: "))
            beneficiary_id = int(input("Enter beneficiary customer ID: "))

            sender = None
            beneficiary = None

            for cus in myCustomersList:
                if cus.cid == sender_id:
                    sender = cus
                if cus.cid == beneficiary_id:
                    beneficiary = cus

            if sender is None:
                print("Sender not found.")
            elif beneficiary is None:
                print("Beneficiary not found.")
            elif sender == beneficiary:
                print("You cannot transfer money to yourself.")
            else:
                amount = float(input("Enter amount to transfer: "))
                sender.transfer_funds(beneficiary, amount)

    elif choice == 4:
        if len(myCustomersList) == 0:
            print("Create a customer first.")
        elif len(myCardsList) == 0:
            print("Create a card first.")
        else:
            for cus in myCustomersList:
                print("ID:", cus.cid, "| Name:", cus.cname)

            customer_id = int(input("Enter customer ID: "))
            found_customer = None

            for cus in myCustomersList:
                if cus.cid == customer_id:
                    found_customer = cus

            if found_customer is None:
                print("Customer not found.")
            else:
                for card in myCardsList:
                    print("Card number:", card.card_no)

                card_number = input("Enter card number to assign: ")
                found_card = None

                for card in myCardsList:
                    if card.card_no == card_number:
                        found_card = card

                if found_card is None:
                    print("Card not found.")
                elif found_card in found_customer.credit_card:
                    print("This card is already assigned.")
                else:
                    found_customer.assign_card(found_card)

    elif choice == 5:
        if len(myCustomersList) == 0:
            print("No customers available.")
        else:
            for cus in myCustomersList:
                cus.display_customer()

    elif choice == 6:
        if len(myCardsList) == 0:
            print("No cards available.")
        else:
            for card in myCardsList:
                card.display_card()

    elif choice == 7:
        print("Exiting program...")
        break

    else:
        print("Invalid choice.")
