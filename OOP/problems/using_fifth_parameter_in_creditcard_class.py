# problem

"""
The CreditCard class of Section 2.3 initializes the balance of a new account to zero. Modify that class so that a new account can be given a
nonzero balance using an optional fifth parameter to the constructor. The
four-parameter constructor syntax should continue to produce an account
with zero balance
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



