# -*- coding: utf-8 -*-
from kort_og_kortstokk import *
"""
from kortstokk import Kort
from kortstokk import Kortstokk

"""

class Hand():
    """
    Klasse for å representere en hånd med kort
    Bruker en ferdig stokket kortstokk for å fylle hånden med kort
        
    """
    
    def __init__(self, navn):
        self.kortPaHand = []
        self.genererHand()
        self.navn = navn
        self.pengesum = 100
    
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
    def visHand2(self):
        """
        Viser hånden til spilleren horisontalt
        """
        liste = self.kortPaHand
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
        returnerer liste med verdier
        """
        """
        finner summen til kortene hånden besitter
        tar hensyn til at ess kan ha flere verdier
        returnerer liste med verdier
        """
        ess = 0
        summer = []    # liste for summene vi skal returnere

        # sjekker hvor mange ess det er på hånda
        for kort in self.kortPaHand:
            if kort.tall == 1:
                ess += 1
                #print("ess - ja")
        
        # hvis ingen ess, regner ut summen
        if ess == 0:
            #print("ess - nei")
            s = 0
            for kort in self.kortPaHand:
                if kort.tall > 10:    # bildekort får verdien 10
                    s += 10
                else: 
                    s += kort.tall
                #print("legger til")
            summer.append(s)

        # hvis ess
        else:
            # legger til summen av alle kortene unntatt essene
            # for så mange muligheter av summer vi kan ha med antall ess
            for j in range(ess+1):
                #print(f"ess - ja, {j}")
                s = 0
                for kort in self.kortPaHand:
                    #print("skal legge til")
                    if kort.tall > 10:
                        s += 10
                    elif kort.tall > 1 and kort.tall <= 10:
                        s += kort.tall
                        
                summer.append(s)

            # regner ut alle mulige verdier for essene
            # og legger disse til på summen
            for k in range(len(summer)):
                summer[k] += (k*11)+((len(summer)-1-k)*1)

        # sorterer listen til synkende verdi
        summer.sort()
        summer.reverse()

        """
        for s in summer:
            if s > 21:
                summer.remove(s)
        """
        # returnerer liste med summer
        return summer
            
    def leggTilKort(self):
        """
        legger til det første kortet i bunken til hånden
        og fjerner kortet fra kortstokken
        """
        self.kortPaHand.append(kortstokk.trekk())
class Dealer(Hand):
    """
    Klasse for dealeren sin hånd
    """
    def __init__(self):
        self.kortPaHand = []
        self.genererHand()   
    
    def visHandDealer(self):
        liste = self.kortPaHand
        tb = "+------+ "
        mid = "|      | "
        
        tbf = tb
        midf = "|??????| "
        con1 = "|??????| "
        con2 = "|??????| "
        farge = ["Kløver","Spar","Hjerter","Ruter"]
        fargeS = ["♣","♠","♥","♦"]

        far = ""
        space = " "

        
        for i in range(len(liste)-1):
            tal = liste[i+1].tall

            if(liste[i+1].tall == 10):
                space = ""
            else:
                space = " "
            if(liste[i+1].tall == 11):
                tal = "J"
            if(liste[i+1].tall == 12):
                tal = "Q"
            if(liste[i+1].tall == 13):
                tal = "K"
            if(liste[i+1].tall == 1):
                tal = "A"
        
            for r in range(len(farge)):
                if(farge[r] == liste[i+1].farge):
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
  

# test for å se om koden fungerer

kortstokk = Kortstokk()
#kortstokk.visKortstokkInfo()
