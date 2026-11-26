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
    print ("Du möter ett par dörrrar. Vilken vill du gå in i?")
    print (f"[1] dörr 1\n[2] dörr 2\n[3] dörr 3")


credits =["credits", "", "", "", "proggrammerare:", "", "Anton Alm","", "Ayane Smith", "", "Hanrui Zhang", "", "", "", ]

lore = """
            Du och din vän utforskade en gammal övergiven fabrik, för att hitta användbara delar av hårdvaror. 
            
            
            
            Din vän hittade en fungerande hiss som går hela vägen upp till högsta våningen.
            
            

            Han gick på hissen och tryckte på våning 10.
            

            
            Du behövde knyta dina skor, så du låter din vän åka upp i förväg. 
            
            
            
            Men hissen kom aldrig tillbaka från våning 10. 
            
            
            Det går inte att ringa din vän för hans mobil dog för 10 minuter sen. 
            
            
            Du bestämmer dig för att använda trapporna i stället. På vägen upp behöver du navigera farliga situationer med fällor, elaka robotar och svåra val.") #Lore
        
            

        """