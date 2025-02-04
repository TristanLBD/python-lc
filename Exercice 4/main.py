from IpValidator import IPValidator
from Bank import Client, BankAccount, AccountManager

def main():
    print('\n\n-------------------- Question 1 --------------------')
    validator = IPValidator()
    validator.askUserForHisIP()
    print('----------------------------------------------------')

    client = Client( ID="69420", firstName="Tristan", name="Leblond")
    bankAccount = BankAccount(owner=client.ID, balance=100)
    accountManager = AccountManager(client, bankAccount)

    print('\n\n-------------------- Question 2 --------------------')
    accountManager.showInfos()
    accountManager.deposit(200)
    accountManager.withdraw(50)
    accountManager.showInfos()
    accountManager.withdraw(1000)
    accountManager.deposit(999999750) # 💲💲💲
    print('----------------------------------------------------')

if __name__ == "__main__":
    main()