import socket
import player
import loop

def playercreator():
    usrin = ""
    incheck = True

    p = player.Player("")

    while incheck:
        print("Please enter your username max 20 char:")
        usrin = input(">")

        if len(usrin) >20 :
            print("I SAID MAX 20 CHAR")
            incheck = True
        else:
            print("Hello ", usrin)
            incheck = False

    p.set_name(usrin)

    return p




def hostgame():
    print("Setting up game...")
    p1 = playercreator()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as ss:
        ss.bind(("localhost", 2048))
        ss.listen()


        print("Launched waiting for player to connect !")

        other, addr = ss.accept()
        with other:

            print("A player has join ! launching game")
            loop.loop(other, p1)


def joingame():
    print("Joining game...")
    p2 = playercreator()

    #a faire : permettre à l'utilisateur de choisir le port et l'addresse
    #pour l'instant on utilise localhost et 2048

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        s.connect(("localhost", 2048))

        print("Connection estalished. Joining game")

        loop.loop(s, p2)







menu = True

usrin = ""
while menu:
    print("Welcome to RPS online 2024 !")
    print("Host (0)")
    print("Join (1)")
    
    usrin = input(">").lower()

    if usrin == "quit":
        menu = False
    elif usrin == "0":
        hostgame()
    elif usrin == "1":
        joingame()
    