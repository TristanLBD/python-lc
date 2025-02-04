from .Client import Client
from .BankAccount import BankAccount

class AccountManager:
    def __init__(self, client: Client, bankAccount: BankAccount):
        self.client = client
        self.bankAccount = bankAccount
    
    def __str__(self):
        return f"Compte de {self.client.name} {self.client.firstName} ({self.client.ID}) : Solde = {self.bankAccount.balance}€"
    
    def showInfos(self):
        print(f"Client : {self.client.name} {self.client.firstName}, ID : {self.client.ID}")
        self.bankAccount.showBalance()
    
    def deposit(self, amount: float):
        self.bankAccount.deposit(amount)
    
    def withdraw(self, amount: float):
        balanceAmount = self.bankAccount.balance
        if balanceAmount < amount:
            print(f"Solde insuffisant ! (Vous avez demandé {amount}€ mais vous ne possedez que {balanceAmount}€.)")
        else:
            self.bankAccount.withdraw(amount)