import pickle
import random

class Customer:
    def __init__(self):
        self.cid = ""
        self.name = ""
        self.acc_no = ""
        self.balance = ""
        self.credit_card = []

    def create_customer(self):
        self.cid = random.randint(1, 100)
        self.name = input("Enter customer name: ")
        self.acc_no = random.randint(100000000000,99999999999)

    def display_customer(self):
        print("CUSTOMER INFORMATION")
        print(self.cid)
        print(self.name)
        print(self.acc_no)
        print(self.balance)

    def transfer_funds(self, bene_cust_obj, amount):
        self.balance -= amount
        bene_cust_obj.balance += amount

    def assign_card (self, card_obj):
        self.credit_card.append(card_obj)

class Card:
    def __init__(self):
        self.card_no = ""
        self.cvv = ""
        self.expiry_month = ""
        self.expiry_year = ""
        self.balance = ""

    def create_card(self):
        self.card_no = random.randint(1, 100)
        self.cvv = random.randint(100,999)
        self.expiry_month = random.randint(1,12)
        self.expiry_year = random.randint(29,35)
        #self.balance

    def display_card(self):
        print("\n CARD INFORMATION")
        print(self.card_no)
        print(self.cvv)
        print(self.expiry_month)
        print(self.expiry_year)
        print(self.balance)

myCustomersList = []
CustomerCardsList = []
myCardsList = []

while True:
    print ("MAIN MENU")
    print ("1. Create Customer Objects")
    print ("2. Create Card Objects")
    print("3. Transfer Funds Between Customer Objects")
    print("4. Assign Card Objects to Customer Objects")
    print("5. Display Customer Info")
    print("6. Display Card Info")
    print("7. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 7:
        print("Exiting...")
        break

    elif choice == 1:
        cus = Customer()
        cus.create_customer()
        myCustomersList.append(cus)

        file1 = open("myCustomers.dat", "ab")
        pickle.dump(cus, file1)
        file1.close()

    elif choice == 2:
        crd = Card()
        crd.create_card()
        myCardsList.append(crd)

        file1 = open("myCards.dat", "ab")
        






