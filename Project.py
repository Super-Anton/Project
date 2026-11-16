# Project om en övergiven ingenjör

# variablar

# Förord
import random
import time

#Klasser
class Spelare():
    def __init__(self):
        self.lvl = 1
        self.str = 5
        self.maxhp = 2*self.lvl + 3
        self.hp = 5
        self.inv = []

    def lvlup(self):
        print ("Du besegrade monstret och lvlade up")
        self.lvl = self.lvl + 1
        self.hp = self.hp + 1
        self.str = self.str + 2

    def inventory_add (self,item):
        if len(self.inv) == 5:
            print ("Ditt inventory är fullt, vad vill du ta bort?")
            for i in self.inv:
                j = self.inv.index(i) + 1
                print (f"[{j}], {i}, ")
            print ("[6] Släng din nya pryl")
            while True:
                item_svar = input("")
                for i in range (0,6):
                    if item_svar == "6":
                        break
                    elif item_svar == str(i+1):
                        self.inv.pop(i)
                        self.inv.append(item)
                    break
        else:
            self.inv.append(item)

        
class Item():
    def __init__(self, name, förklaring, bonus):
        self.name = name
        self.förklaring = förklaring
        self.bonus = bonus
    def item_info(self):
        print(f"{self.name}")
        print(f"{self.förklaring}")
        print(f"Du får +{self.bonus} till din STR")

    
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

def open_door ():
    results = ["Monster", "Trap", "Chest"]
    weights = [5,2,3]
    picked_door = random.choice (results, weights=weights, k=1) [0]
    if picked_door == "Monster":
        print ("Det finns en monster bakom dörren. Bakom den ser du trappan till nästa våning.")
    elif picked_door == "Trap":
        possible_trap = ["Du rörde handtaget och PANG exploderade bomben bakom den. Du tar ", "Du rörde handtaget och den var ", "Du rörde handtaget och den var xxxxx"]
        trap = random.choice(possible_trap, k=1) [0]
        print (trap)
    elif picked_door == "Chest":
        print ("Det finns en kista bakom dörren. ")
    return (picked_door)

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
svar_dörr = input("")
if svar_dörr == "1" or svar_dörr == "2" or svar_dörr == "3":
    open_door()