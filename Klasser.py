#Klasser
class Player():
    def __init__(self,lvl,str,hp,inv):
        self.lvl = lvl
        self.str = str
        self.maxhp = 2*lvl + 3
        self.hp = hp
        self.inv = inv

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

    def inv_print (self):
        for i in self.inv:
            print(i, end=" ")
    
    def skada(self,antal):
        self.hp = self.hp - antal

    def return_värde(self, attribut):
        if attribut == "lvl":
            return self.lvl
        elif attribut == "str":
            return self.str
        elif attribut == "hp":
            return self.hp

class Item():
    def __init__(self, name, förklaring, bonus):
        self.name = name
        self.förklaring = förklaring
        self.bonus = bonus
        
    def item_info(self):
        print(f"{self.name}")
        print(f"{self.förklaring}")
        print(f"Du får +{self.bonus} till din STR")

    def return_name(self):
        return (self.name)