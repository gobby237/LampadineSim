
import random

# tutte le lampadine sono spente, adesso volta per volta devo accendere una lampadina a caso 
counter = 0
n = int(input("Inserire numero di ripetizioni: "))
for t in range (0,n):

    lamp = [False] * 100

    for i in range (0,100):
        index = random.randint(0,99) # genero un numero casuale tra 0 e 99 

        if (lamp[index] == False):
            lamp[index] = True
        else:
            if (lamp[index] == True): 
                lamp[index] = False

    spento = True

    for i in lamp: 
        if (i == True):
            spento = False

    if (spento == True): 
        counter += 1

# visualizzo counter 

print("RISULTATO:\n" + str(counter) + " tutte spente \n" +str(n)+  " totali")



