import time

def start_test():
    print ("Välkommen till vårat spel")
    print ("[1] Börja spela")
    print ("[2] Lore")
    print ("[3] Credits")
    print ("[4] Lämna")


def slow_print (message):
    for i in message:
        print (i, end="", flush=True)
        time.sleep(0.1)

def dörr_text():
    print ("Du kommer öppnar dörren till fabriken och möter ett par dörrrar. Vilken vill du gå in i?")
    print (f"[1] dörr 1\n[2] dörr 2\n[3] dörr 3")
