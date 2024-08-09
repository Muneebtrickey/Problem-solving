# Project
# Problem


"""
Write a Python program that can “make change.” Your program should
take two numbers as input, one that is a monetary amount charged and the
other that is a monetary amount given. It should then return the number
of each kind of bill and coin to give back as change for the difference
between the amount given and the amount charged. The values assigned
to the bills and coins can be based on the monetary system of any current
or former government. Try to design your program so that it returns as
few bills and coins as possible.
"""


"""
step1: Understand the problem clearly and precisely. Identify inputs and outputs formats. 


    problem: 
        we need to implement a python program which take two parameters the first one is monetary charge (means that those price which is set by the seller to sell something)
        and the second one is monetary given ( means those payment which we pay to buy the things). so the problem is asking us if the monetary given price is greater than the monetary charge price so we need to give back the extra amount. so how can we give it back we will use a monetary system in which we have bills and coins so from these we will give him money back. But the important thing in this is that we need to give back the money using minimum bills and coins.



        formats: 
        input: 
            monetary charge: The price which is set by the seller
            monetary given : The payment we pay for the thing to buy. 
        
        output:
             If the monetary charge and monetary given is equal so we will just print that transcation successful and everything is ok. 

             if the monetary given is greater we need to given back the money using minimum bills and coins. so it means that we will return the bills and coins and the sum of the bills and coins. 
            
"""


"""
step2: come up with some examples inputs and outputs and try to cover all edges cases. 

format: 
    def make_change(monetary_charge, monetary_given):
          pass


"""

tests =  []

# if both the monetary price is zero

tests.append({
    "input":{
        "monetary_charge": 0,
        "monetary_given": 0
    },
    "output": "The Product is Free"
})



# if the monetary_charge and monetary_given is equal

tests.append({
    "input": {
        "monetary_charge": 50,
        "monetary_given": 50
    },
    "output": "Transcation successful and Everything is ok"
})


# if the monetary_given is greater than the monetary_charge

tests.append({
    "input": {
        "monetary_charge": 50,
        "monetary_given": 80
    },
    "output": 30 
})





"""
step3: come up with a correct solutio and state it in plain english. 

Algorithm: 
         1. First of all we will check that if the monetary_charge and monetary_given is zero so return "The Product is Free".

         2. if the monetary_charge and monetary_given is equal so return "Transcation successful and Everyting is ok" 

         3. else if the monetary_given is greater than the monetary_charge so we need to do the following things. 
            * first of all we will create a variable and name it
               given and store the given value like 
                given = monetary_given - monetary_charge
                so the extra money which will be given to the user is
                stored in it. 

            * now we will create another variable name given_from_bills_and_coins = 0 . initialy it will be zero. 

            * we will create another List_of_bills in which bills and coins will be stored whose are used to give money back to the user. 

            * now we will create a list of bills and coins which will store the monetary system so i am using usa monetary system. 
                 monetary_system = [100, 50, 20, 10, 5, 1, 0.25, 0.10, 0.05, 0.01]

            
            * Now we will apply loop inside the loop we will write 
             this condition that
                 i = 0
                 while True:
                      if monetary_system[i] > given:
                            pass
                      else:

                          given = given - monetary_system[i]
                          given_from_bills_and_coins += monetary_system[i]
                          List_of_bills_which_given.append(monetary_system[i])
                          i = 0

                    if given_from_bills_and_coins == (monetary_given-charge):
                    break
                    i += 1

                
            * after completion of the loop return given_from_bills_and_coins, List_of_bills_which_given

                      

"""


"""
ste4: Implement the solution and fix bugs if any. 
"""
from time import time


def make_change(monetary_charge, monetary_given):
    if monetary_charge  == 0 and monetary_given == 0:
        return "This Product is Free"
    
    if monetary_charge == monetary_given:
        return "Transcation successful and Everything is ok"
    
    elif monetary_charge > monetary_given:
        return "You must need to pay the full price."
    
    else:
        given = monetary_given - monetary_charge
        given_from_bills_and_coins = 0
        List_of_bills_and_coins = []
        monetary_system = [100, 50, 20, 10, 5, 1, 0.25, 0.10, 0.05, 0.01]

        i = 0
        while True:
            if monetary_system[i] > given:
                pass
            else:
                given_from_bills_and_coins += monetary_system[i]
                List_of_bills_and_coins.append(monetary_system[i])
                given = given - monetary_system[i]
                i = 0  # again start from the start. 
            if given_from_bills_and_coins == (monetary_given - monetary_charge):
                break
            i += 1
        
        
        return given_from_bills_and_coins, List_of_bills_and_coins


start_time = time()
print(make_change(50,80))
end_time = time()

print("Start time: ", start_time)
print("End time: ", end_time)
print("Total time: ", end_time - start_time)
        



