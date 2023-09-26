class Bank:
    bank_name = "NMB"
    rate_of_interest =20.22
    @staticmethod
    def simpleInterest(p,t):  #static method dont use 'self'
        si=(p*t*Bank.rate_of_interest)/100
        print(si)

p=float(input("Enter Principal:"))
t=int(input("Enter time interval:"))
Bank.simpleInterest(p,t)