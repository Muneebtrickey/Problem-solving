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
        self.balance = 10
    

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

    
    # this is a task  , we need to create a non_public method which set the balance

    def _set_balance(self,balance):
        self.balance = balance
    


            





creditcard = CreditCard("muneeb","meezan bank",9999999,100)

# print(creditcard.get_customer_name())
# print(creditcard.get_bank_name())
# print(creditcard.get_account_number())
# print(creditcard.get_account_limit())
# print(creditcard.get_balance())

# 
# lets add some money in my account 

# print(creditcard.charge(50.0))


# now check that the amount is added or not

# print(creditcard.get_balance())



# problem


"""
The PredatoryCreditCard class of Section 2.4.1 provides a process month
method that models the completion of a monthly cycle. Modify the class
so that once a customer has made ten calls to charge in the current month,
each additional call to that function results in an additional $1 surcharge.
"""

from datetime import datetime



class PredatoryCreditCard(CreditCard):
    OVER_LIMIT_FEE = 5
    def __init__(self, customer , bank , account , limit , minimum_payment):
        super().__init__(customer, bank, account, limit)
        self._counts = 0
        self._current_month = datetime.now().month
        self._customer_montly_payment = 0
        self._payment_made = 0
        self._minimum_payment = minimum_payment



    def charge(self,price: int):

        if self._current_month != datetime.now().month:
            self._counts = 0
            self._current_month = datetime.now().month
        
        success = super().charge(price)

        if success:

            self._counts += 1
            
            if self._counts > 10:
                self._balance += 1 # 1 dollar surcharge is added
            
        else:
            self._balance += PredatoryCreditCard.OVER_LIMIT_FEE
        
        return success
    

    def find_minimum_payment(self):

        self._customer_montly_payment = (self._minimum_payment / 100)  * self._balance 
    

    def process_month(self):

        if self._current_month != datetime.now().month:

            if self._payment_made < self._customer_montly_payment:
                self._customer_montly_payment  += 10 # 10 dollar will be  late fee
            

            # now we are resetting for the new month

            self._payment_made = 0
            # now we are set the new month
            self._current_month = datetime.now().month
            self.find_minimum_payment()




pcredit = PredatoryCreditCard("Muneeb","meezan", 219393,100,10)
print(pcredit.get_balance())


# now we are setting the balance

print(creditcard.get_balance())

# now we are setting the balance

creditcard._set_balance(30)


# now we are printing agian the balance

print(creditcard.get_balance())


   

        

    

