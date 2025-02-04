class BankAccount:
    def __init__(self, owner: str, balance: float = 0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount: float):
        if amount > 0:
            self.balance += amount
            print(f"Dépôt de {amount} effectué. Nouveau solde : {self.balance}€")
        else:
            print("Le montant du dépôt doit être positif.")
    
    def withdraw(self, amount: float):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Retrait de {amount} effectué. Nouveau solde : {self.balance}€")
        else:
            print("Montant insuffisant ou invalides.")
    
    def showBalance(self):
        print(f"Solde actuel : {self.balance}€")