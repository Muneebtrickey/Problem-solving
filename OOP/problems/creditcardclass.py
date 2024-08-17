# problem

"""
Use the techniques of Section 1.7 to revise the charge and make payment
methods of the CreditCard class to ensure that the caller sends a number
as a parameter.
"""


"""now we are creating a creditcard class """



class CreditCard:
    "A consumer creditcard"
    def __init__(self, customer : str , bank : str , account : int , limit : int):
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
            





creditcard = CreditCard("muneeb","meezan bank",9999999,100)

print(creditcard.get_customer_name())
print(creditcard.get_bank_name())
print(creditcard.get_account_number())
print(creditcard.get_account_limit())
print(creditcard.get_balance())


# lets add some money in my account 

print(creditcard.charge(50.0))


# now check that the amount is added or not

print(creditcard.get_balance())


