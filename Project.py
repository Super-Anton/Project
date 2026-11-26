# Project om en övergiven ingenjör


# importeringar
import sys
import random
import time
import Print_modul
import Klasser


# Klasser
spelare = Klasser.Player(1,5,50,[])  #lvl,str,hp,inv


laserpistol = Klasser.Item("laserpistol", "Den är miljövänlig för att den går på el. Du kan sjuta ihjäl monster enkelt", 7)
axe = Klasser.Item("Yxa", "chopp chopp chopp.", 6)
matkniv = Klasser.Item("matkniv", "Öka din skada med denna vassa egg", 5)
metallstav = Klasser.Item("metallstav", "stav av metall.", 4)
bunch_of_cats = Klasser.Item("katter", "Hissande konpanioner som använder sina vassa klor för dig.", 3)
vapen_som_gör_2_skada = Klasser.Item("Vapen som gör 2 skada", "Det behövs ingen annan förklaring.", 2)
plastkniv = Klasser.Item("plastkniv", "Bättre än inget... eller så är inget bättre.", 1)
skit = Klasser.Item("skit.", "Inget är definitivt bättre.", 0)
items = [laserpistol, axe, matkniv, metallstav, bunch_of_cats, vapen_som_gör_2_skada, plastkniv, skit]

# Funktioner
def dice (min,max):
    slumptal = random.randint(min,max)
    return slumptal

def chest (spelare: Klasser.Player):
    in_chest = ["heal", "strength_bonus", "item"]
    weight = [3, 5, 2]
    chest_resultat = random.choices(in_chest, weights=weight, k=1) [0]
    if chest_resultat == "heal":
        spelare.hp = spelare.hp + 5
        print ("Du hittade ett elixir som gav dig 5 hälsa")
    elif chest_resultat == "strength_bonus":
        spelare.str = spelare.str + 2
        print ("Du hittade ett elixir som gav dig 2 str")
    elif chest_resultat == "Item":
        weight = [1, 2, 3, 4, 5, 5, 2]
        picked_item = random.choices(items, weights=weight, k=1) [0]
        return(picked_item)
    

def open_door ():
    results = ["Monster", "Trap", "Chest"]
    weight = [5,2,3]
    picked_door = random.choices(results, weights=weight, k=1) [0]
    if picked_door == "Monster":
        print ("Det finns en monster bakom dörren. Bakom den ser du trappan till nästa våning.")
    elif picked_door == "Trap":
        possible_trap = ["Du rörde handtaget och PANG exploderade bomben bakom den. Du tar ", "Det var en elak dörr! Dörren slår dig! Du tar ", "Elkablen ramlade på handtaget och du fick en el-shock. Du tar ", "Så fort du rörde handtaget föll det ner en sten från taket. Du tar ", "Det finns en kista bakom dörren. Du går till kistan. Kistan BITER DIG! Jävla Mimic! du tar ", "Det finns en kista bakom dörren. Du går till kistan. Kistan BITER DIG! Jävla Mimic! du tar "]
        trap = random.choices(possible_trap, k=1) [0]
        Print_modul.slow_print(trap)
        trap_damage = dice (1,5)
        print(f"{trap_damage} skada.")
        spelare.skada(trap_damage)
    elif picked_door == "Chest":
        Print_modul.slow_print("Det finns en kista bakom dörren. ")
    return (picked_door)


def create_monster(spelare: Klasser.Player):
    monster_str = dice(3,7) + 2 * spelare.lvl
    return monster_str


def fight(spelare: Klasser.Player, monster_str):
    if monster_str < spelare.str:
        print ("Du besegra monstret! Gå upp för trappan för att rädda ditt vän nu.")
        spelare.lvlup()
    elif monster_str - spelare.str < 2:
        print (f"Nästan! den var bara lite starkare än dig. Du tar {monster_str-spelare.str} skada.")
        return (monster_str - spelare.str)
    elif monster_str - spelare.str < 4:
        print (f"Oof, Den var mycket starkare än dig. Du tar {monster_str - spelare.str} skada.")
        return (monster_str - spelare.str)
    else:
        print (f"ouch, Den var oerhört stark. Du tar {monster_str - spelare.str} skada.")
        return (monster_str - spelare.str)


def check_hp(spelare: Klasser.Player):
    if spelare.hp <= 0:
        print ("Du Dog....")

def check_win(spelare: Klasser.Player):
    if spelare.lvl == 10:
        return True
    else:
        return False

def try_int (sträng):
    try:
        sträng = int(sträng)
    except:
        print ("du måste skriva siffor")
    return sträng

def exit():
    print("Du lämnade rummet och kände hur den ändrades bakom dig.")
    

#HuvudProgram
# Start meny

Print_modul.start_test()
while True:
    svar_start = input ("")
    svar_start = try_int(svar_start)
    if svar_start == 1:
        break
    elif svar_start == 2:
        Print_modul.slow_print(Print_modul.lore)
    elif svar_start == 3:
        for i in Print_modul.credits:
            print(Print_modul.credits[i])
            time.sleep(0.2)
    elif svar_start == 4:
        print ('"Only winning move is not to play - tzun szu"')
        sys.exit()

# Startat spel
while True:  # Det här är ett test
    Print_modul.dörr_text()
    svar_dörr = input ("")
    svar_dörr == try_int(svar_dörr)

    if svar_dörr == "1" or svar_dörr == "2" or svar_dörr == "3":
        rum = open_door()
        if rum == "Chest":
            chest_result = chest(spelare)
            if chest_result in items:
                spelare.inventory_add(chest_result)
        elif rum == "Monster":
            print (f"Du ser ett läskigt monster. \n Vad vill du göra? \n [1] Slåss \n [2] lämna")
            monster_svar = input ("")
            monster_svar == try_int(monster_svar)
            if monster_svar == "1":
                fight(spelare,create_monster(spelare))
            elif monster_svar == "2":
                exit()
    elif svar_dörr == "inv":  # Denna del funkar inte
        spelare.inv_print()