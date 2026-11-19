# Project om en övergiven ingenjör

# variablar

# Förord
import random
import Print_modul
import Klasser

# Klasser
spelare = Klasser.Player(1,5,5,[])

svärd = Klasser.Item("svärd", "Öka din skada med denna vassa egg", 5)
metallstav = Klasser.Item("metallstav", "stav av metall.", 4)
katt = Klasser.Item("katt", "En hissande konpanion som använder ens vassa klor för dig.", 3)
vapen_som_gör_2_skada = Klasser.Item("Vapen som gör 2 skada", "Det behövs ingen annan förklaring.", 2)
plastkniv = Klasser.Item("plastkniv", "Bättre än inget... eller så är inget bättre.", 1)
laserpistol = Klasser.Item("laserpistol", "Den är miljövänlig för att den går på el. Du kan sjuta ihjäl monster enkelt.", 7)
skit = Klasser.Item("skit." "Inget är definitivt bättre.", 0)

# Funktioner
def Dice (min,max):
    slumptal = random.randint(min,max)
    return slumptal

def chest ():
    in_chest = ["heal", "strength_bonus", "item"]
    items = ["axe", "thicker_cloth", "bunch_of_cats", "pistol"]
    weight = [3 ,5 ,2]
    picked_item = random.choices(in_chest, weights=weight, k=1) [0]
    if picked_item == "item":
        picked_item = random.choices(items, k=1) [0]
    return(picked_item)

def open_door ():
    results = ["Monster", "Trap", "Chest"]
    weight = [5,2,3]
    picked_door = random.choices(results, weights=weight, k=1) [0]
    if picked_door == "Monster":
        print ("Det finns en monster bakom dörren. Bakom den ser du trappan till nästa våning.")
    elif picked_door == "Trap":
        possible_trap = ["Du rörde handtaget och PANG exploderade bomben bakom den. Du tar ", "Det var en elak dörr! Dörren slår dig! Du tar ", "Du rörde handtaget och den var xxxxx. Du tar "]
        trap = random.choices(possible_trap, k=1) [0]
        print (trap, end="")
        trap_damage = Dice (1,5)
        print(f"{trap_damage} skada.")
        spelare.skada(trap_damage)
    elif picked_door == "Chest":
        print ("Det finns en kista bakom dörren. ")
        
    return (picked_door)

def Monster():
    spelar_str = Klasser.spelare.return_värde("lvl")
    monster_str = Dice(3,7) + 2 * spelar_str
    return monster_str

def Fight(player_str, monster_str):
    if player_str > monster_str:
        Klasser.spelare.lvlup
    elif monster_str - player_str < 2:
        print (f"Nästan den var bara lite starkare än dig, Du tar {monster_str-player_str} skada")
        spelare.skada(monster_str - player_str)
    elif monster_str - player_str < 4:
        print (f"Oof, Den var mycket starkare än dig, Du tar {monster_str - player_str} skada")
        spelare.skada(monster_str - player_str)
        
def check_hp():
    if Klasser.spelare.return_värde("hp") <= 0:
        print ("du dog")
    


#HuvudProgram
Print_modul.start_test()
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
Print_modul.dörr_text()

svar_dörr = input("")
if svar_dörr == "1" or svar_dörr == "2" or svar_dörr == "3":
    spelare.inventory_add(katt)
    spelare.inventory_add(svärd)
    spelare.inv_print()