import random

nmin = int(input("Inserisci il numero più piccolo da indovinare "))
nmax = int(input("Inserisci il numero più grande da indovinare "))

numero_lelloso = random.randint(nmin,nmax)
tentativitemp = nmax - nmin
if tentativitemp <= 100:
    tentativimax = 10
else:
     tentativimax=15
     
#tentativimax = 10
tentativi = 0
print("Indovina il numero tra" , nmin ," e " , nmax)
while tentativi < tentativimax:
    rimasti = tentativimax - tentativi
    scelta = int(input(f"Tentativi rimasti {rimasti} "))
    if scelta == numero_lelloso:
        print("Hai indovinato il numero Lelloso è", numero_lelloso)
        break
    elif numero_lelloso < scelta:
        print("Il numero Lelloso è piu basso")    
    elif numero_lelloso > scelta:
        print("Il numero Lelloso è piu alto")    
    tentativi += 1
if tentativi == 0:
        print("hai perso il numero Lelloso era:",numero_lelloso)     
