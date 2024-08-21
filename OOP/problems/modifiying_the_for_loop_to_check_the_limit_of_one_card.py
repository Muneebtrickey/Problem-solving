# problem

"""
Modify the declaration of the first for loop in the CreditCard tests, from
Code Fragment 2.3, so that it will eventually cause exactly one of the three
credit cards to go over its credit limit. Which credit card is it?
"""



class CreditCard:
    "A consumer creditcard"
    def __init__(self, customer : str , bank : str , account : int , limit : int, balance = 0):
        """
        create a new creditcard instance
        the initial balance is zero

        customer , the name of the customer
        bank , the bank name of the customer  (meezan bank)
        account , the account number of the customer
        limit , the account limit of the customer
        
        """

        self.customer_name = customer
        self.bank_name = bank
        self.account_number = account
        self.account_limit = limit
        self.balance = 0
        self.balance = balance
    

    def get_customer_name(self):
        """ Return name of the customer"""
        return self.customer_name
    
    
    def get_bank_name(self):
        """Return customer bank name. """
        return self.bank_name
    
    
    def get_account_number(self):
        """return customer account number"""
        return self.account_number
    
    def get_account_limit(self):
        """return account limit"""
        return self.account_limit
    

    def get_balance(self):
        """return customer account balance"""
        return self.balance
    
    
    def charge(self,price):
        """
        checking that the price is number or float not str
        charge given to the card ,  assuming sufficent creditcard limit

        Return True if charge was process , False if charge was denied
        """

        if isinstance(price, int | float): # tuple (int,float)
            if price + self.balance > self.account_limit:
                return False
            else:
                self.balance += price
                return True
        else:
            return "The price must be int type."
    
    def make_payment(self,amount):
        """process customer amount to reduce balance"""
        if isinstance(amount,int | float): # tuple (int, float)
            self.balance -= amount
        
        else:
            return "amount must be int."
            





creditcard = CreditCard("muneeb","meezan bank",9999999,10000,500)

print(creditcard.get_balance())




# lets create a list which will store three cards

wallet = []

wallet.append(creditcard)
creditcard1 = CreditCard("anees","MCB",7777777,1500,40)
creditcard2 = CreditCard("imran","JS bank",66666, 200,50)
wallet.append(creditcard1)
wallet.append(creditcard2)


# now we will apply loop and add the amount in the card

for i in range(20):
    card1 = wallet[0].charge(i*2)
    card2 = wallet[1].charge(i**2)
    card3 = wallet[2].charge(i ** 1.5)
    
    # now we are checking that if the card1 return false so it 
    # means the card limit is complete and so on

    if not card1:
        break
    elif not card2:
        break
    elif not card3:
        break


if not card1:
    print("card1 limit is exceed")

elif not card2:
    print("card2 limit is exceed")

elif not card3:
    print("card 3 limit is exceed")

else:
    print("no card limit is execeed")


