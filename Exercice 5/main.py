from Dealer import Dealer

def main():
    
    try:
        numPlayers = int(input("Combien y a t'il de joueurs ? "))
        dealer = Dealer(numPlayers)
        print(dealer)
    except Exception as e:
        print(e)
    
if __name__ == "__main__":
    main()