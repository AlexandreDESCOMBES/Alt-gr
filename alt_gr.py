import keyboard
import pyperclip



def credits():
    print("Developped by Alexandre")         #Display credits


# -- fonctions de callbacks des raccourcies --

def copiePressePapier3(): 
    print("copie3")
    pyperclip.copy("#")
    
def copiePressePapier4(): 
    print("copie4")
    pyperclip.copy("{}")
    
def copiePressePapier5(): 
    print("copie5")
    pyperclip.copy("[]")
    
def copiePressePapier6(): 
    print("copie6")
    pyperclip.copy("|")
    

    
def copiePressePapier0(): 
    print("copie0")
    pyperclip.copy("@")
    

def main():
    #Moteur
    credits()
    while True:
        # -- enregistrement des évènements liés aux raccourcies clavier --
        keyboard.add_hotkey("ctrl + 3", copiePressePapier3) 
        keyboard.add_hotkey("ctrl + 4", copiePressePapier4)
        keyboard.add_hotkey("ctrl + 5", copiePressePapier5)
        keyboard.add_hotkey("ctrl + 6", copiePressePapier6)
        keyboard.add_hotkey("ctrl + 0", copiePressePapier0)

        keyboard.wait() # attente infinie 

if __name__ == "__main__":
    main()