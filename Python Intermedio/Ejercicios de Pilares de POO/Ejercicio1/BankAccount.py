#Cree una clase de BankAccount que:
#Tenga un atributo de balance.
#Tenga un método para ingresar dinero.
#Tengo un método para retirar dinero.


#necesito que la cuenta de banco se le agregue dinero , que yo lo agregue 
#necesito que el balance se modifique dependiendo de el metodo 
#necesito que funcione en diferentes cuentas de banco 



class BankAccount(): 
    
    #balance = 0 : haría que todas tengan el mismo balance
    
    def __init__(self, balance): #Cada objeto tiene su propio balance
        self.balance = balance
        
    def add_money(self, amount):
        if amount > 0:
            self.balance += amount
            print("You have added this amount to your bank account ", amount) 
        else:
            print("Invalid amount")
            
    def rest_money(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print("You have taken this amount from your bank account ", amount) 
        else:
            print("Insufficient funds")
        
myAccount = BankAccount(0)
myAccount.add_money(23)
print("My balance: ",myAccount.balance)
        
myAccount.rest_money(2)
print("My balance: ",myAccount.balance)  


class SavingsAccount(BankAccount):
    def __init__(self, balance, min_balance): #Cada objeto tiene su propio balance
        super().__init__(balance)
        self.min_balance = min_balance
        
    def rest_money(self, amount):
        if amount > 0:
            if self.balance - amount < self.min_balance:
                print("Insufficient funds")
            else:
                self.balance -= amount
                print("You have taken this amount from your bank account ", amount) 
                
                
mySavingsAccount = SavingsAccount(40,10)
mySavingsAccount.rest_money(20)
mySavingsAccount.rest_money(15)

print("My balance: ",mySavingsAccount.balance)  