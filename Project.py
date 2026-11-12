# Project om en övergiven ingenjör

# variablar
inv = []

# Förord
import random
import time

#Klasser

# Funktioner
def Dice (min,max):
    slumptal = random.randint(min,max)
    return slumptal

def chest ():
    in_chest = ["heal", "strength_bonus", "item"]
    items = ["axe", "thicker_cloth", "bunch_of_cats", "pistol"]
    weights = [3 ,5 ,2]
    picked_item = random.choices(in_chest, weights=weights, k=1) [0]
    if picked_item == "item":
        picked_item = random.choices(items, k=1) [0]
    return(picked_item)

def inventory_add (item):
    if len(inv) == 5:
        print ("Ditt inventory är fullt, vad vill du ta bort?")
        for i in inv:
            j = inv.index(i) + 1
            print (f"[{j}], {i}, ")
        print ("[6] Släng din nya pryl")
        while True:
            item_svar = input("")
            if item_svar == "1":
                inv.pop(0)
                inv.append (item)
                break
            elif item_svar == "2":
                inv.pop(1)
                inv.append (item)
                break
            elif item_svar == "3":
                inv.pop(2)
                inv.append (item)
                break
            elif item_svar == "4":
                inv.pop(3)
                inv.append (item)
                break
            elif item_svar == "5":
                inv.pop(4)
                inv.append (item)
                break
            elif item_svar == "6":
                break
    else:
        inv.append(item)

#HuvudProgram
print ("Välkommen till vårat spel")
print ("[1] Börja spela")
print ("[2] Lore")
print ("[3] Credits")
print ("[4] Lämna")
while True:
    svar_start = input ("")
    try:
        svar_start = int(svar_start)
        if svar_start == 1:
            break
        elif svar_start == 2:
            print ("Du och din vän utforskade en gammal övergiven fabrik, för att hitta användbara delar av hårdvaror. Din vän hittade en fungerande hiss som går hela vägen upp till högsta våningen, och han gick på hissen och tryckte på våning 10. Du behövde knyta dina skor, så du låter din vän åka upp i förväg. Men hissen kom aldrig tillbaka från våning 10. Det går inte att ringa din vän för hans mobil dog för 10 minuter sen. Du bestämmer dig för att gå upp för trapporna i stället. På vägen behöver du navigera farliga situationer med fällor, elaka robotar och svåra val.") #Lore
        elif svar_start == 3:
            print ("") # Credits
        elif svar_start == 4:
            print ('"Only winning move is not to play - tuzn szu"')
    except:
        print ("du måste skriva en siffra")

# Startat spel
print ("Du kommer öppnar dörren till fabriken och möter ett par dörrrar. Vilken vill du gå in i?")
print (f"[1] dörr 1\n[2] dörr 2\n[3] dörr 3")
print (chest())