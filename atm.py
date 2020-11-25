class Atm(object):
    def __init__  (self, cardNumber, cardPin ):
        self.cardNumber = cardNumber
        self.cardPin  = cardPin
     
    def withdrawal(self):
        amount = input("how much do you want to withdraw")
        w = "You have withdrawn {} rupees".format(amount)
        print(w)

atm = Atm(input("Enter Card Number"),input("Enter Pin"))
print(atm.withdrawal())
