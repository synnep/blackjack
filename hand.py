# -*- coding: utf-8 -*-
from kortstokk import Kort
from kortstokk import Kortstokk

class Hand():
    """
    Klasse for å representere en hånd med kort

    Bruker en ferdig stokket kortstokk for å fylle hånden med kort
        
    """
    
    def __init__(self):
        self.kortPaHand = []
        self.genererHand()
    
    def genererHand(self):
        """
        genererer en hånd med to kort
            de to øverste kortene fra en ferdig stokket kortstokk
        """
        for i in range(2):
            self.kortPaHand.append(kortstokk.trekk())
    
    def visHand(self):
        """
        viser kortene hånden sitter på
        """
        for k in self.kortPaHand:
            k.visKortInfo()
    def visHand2(self, liste):
        tb = "+------+ "
        mid = "|      | "
        
        tbf = ""
        midf = ""
        con1 = ""
        con2 = ""
        farge = ["Kløver","Spar","Hjerter","Ruter"]
        fargeS = ["♣","♠","♥","♦"]

        far = ""
        space = " "

        
        for i in range(len(liste)):
            tal = liste[i].tall

            if(liste[i].tall == 10):
                space = ""
            else:
                space = " "
            if(liste[i].tall == 11):
                tal = "J"
            if(liste[i].tall == 12):
                tal = "Q"
            if(liste[i].tall == 13):
                tal = "K"
            if(liste[i].tall == 1):
                tal = "A"
        
            for r in range(len(farge)):
                if(farge[r] == liste[i].farge):
                    far = fargeS[r]
            tbf += tb
            midf += mid
            con1 += f"| {tal}{space} {far} | "
            con2 += f"| {far}  {tal}{space}| "
        print(tbf)
        print(con1)
        print(midf)
        print(midf)
        print(con2)
        print(tbf)
    def finnSum(self):
        """
        finner summen til kortene hånden besitter
        tar hensyn til at ess kan ha flere verdier
        !! returnerer ingen verdi, kun print
        """
        ess = "nei"

        for kort in self.kortPaHand:
                if kort.tall == 14:
                    ess = "ja"
        
        if ess == "ja":
            s1 = 0
            s2 = 0
           
            for kort in self.kortPaHand:
                s1 += kort.tall
                print(s1)
         
            for kort in self.kortPaHand:
                if kort.tall == 14:
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
            
  def leggTilKort(self):
        """
        legger til det første kortet i bunken til hånden
        og fjerner kortet fra kortstokken
        """
        self.kortPaHand.append(kortstokk.trekk())


# test for å se om koden fungerer

kortstokk = Kortstokk()
#kortstokk.visKortstokkInfo()

h1 = Hand()

h1.visHand()
h1.finnSum()
