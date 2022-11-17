# Ikke fullstendig!!

from kortstokk import Kortstokk

kortstokk = Kortstokk()
kortstokk.visKortstokkInfo()

class Hand():
    
    def __init__(self):
        self.kortPaHand = []
        self.genererHand()
    
    def genererHand(self):
        for i in range(2):
            self.kortPaHand.append(kortstokk.trekk())
    
    def visHand(self):
        for kort in self.kortPaHand:
            kort.visKortInfo()
    
    def finnSumm(self):
        ess = "nei"
        for kort in self.kortPaHand:
                if kort.tall == 13:
                    ess = "ja"
                else:
                    print("Det er ikke et ess")
        
        if ess == "ja":
            print("Det er et ess")
            s1 = 0
            s2 = 0
           
            for kort in self.kortPaHand:
                s1 += kort.tall
                print(s1)
         
            for kort in self.kortPaHand:
                if kort.tall == 13:
                    s2 += 1
                else:
                    s2 += kort.tall
            print("Sum med 13: ", s1)
            print("Sum med 1: ", s2)
        else: 
            s = 0
            for kort in self.kortPaHand:
                s += kort.tall
            print(s)


hand1 = Hand()
print()
print(hand1)
print()
print(hand1.visHand())

print(len(hand1.kortPaHand))
print()

hand1.finnSumm()


