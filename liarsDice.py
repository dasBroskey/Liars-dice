import random
from player import Player
import tkinter as tk

def popupmsg(msg, title):
    root = tk.Tk()
    root
    root.title(title)
    label = tk.Label(root, text=msg)
    label.pack(side="top", fill="x", pady=20,padx=120)
    B1 = tk.Button(root, text="Okay", command = root.destroy)
    B1.pack()
    root.mainloop()


def nextplayer(players,player1):
    if player1 + 1 > players-1:
        player2 = 0
    else:
        player2 = player1+1
    return player2

players = int(input("How many players? "))
start_dice = int(input("How many starting dice? "))
playerslist = []

#Initialize game

#choose first player
firstplayer = random.randint(0,players-1)
guessplayer = firstplayer
lieplayer = nextplayer(players,firstplayer)

#Create players
for i in range(players):
    name = input(f"What is player {i+1}'s name? ")
    playerslist.append(Player(name,start_dice))

#Roll dice
for person in playerslist:
    person.mix()

while len(playerslist) > 1: #--loop--
#   Ask player for guess

    title = (f"~~ {playerslist[guessplayer].get_name()}'s turn.~~")
    message = playerslist[guessplayer].get_dice()
    popupmsg(message,title)
    (f"~~ {playerslist[guessplayer].get_name()}'s turn.~~")
    playerslist[guessplayer].make_guess()
#   Ask next player for lie or guess
    title = (f"~~ {playerslist[lieplayer].get_name()}'s turn~~")
    message = playerslist[lieplayer].get_dice()
    popupmsg(message,title)
    print(f"~~ {playerslist[lieplayer].get_name()}'s turn~~")
    call = input('call a "lie" or "guess"? ')
    #variable for valid answer
    goodans = False
    #ask until good answer
    while not goodans:

        #if lie
        if call == 'lie':
            goodans = True
            #Reveal dice
            guess_tup = playerslist[guessplayer].get_guess()
            die_num = guess_tup[0]
            die_ammount = guess_tup[1]
            total = 0
            #count dice for number guess
            for gamer in playerslist:
                total += gamer.get_cup(die_num)
            #if number dice less than count
            if total < die_ammount:
                #lie player loses one die
                playerslist[guessplayer].remove_die()
            #else
            else:
                #guess player loses one die
                playerslist[lieplayer].remove_die()
            for person in playerslist:
                person.mix()
        #if guess
        elif call == 'guess':
            goodans = True
            #store as guessplayer
            guessplayer = lieplayer
            lieplayer = nextplayer(players,guessplayer)
            pass
        if goodans == False:
            call = input('Please type either "lie" or "guess"')
        #Make sure all players have at least 1 die
    player_out = None
    for i_player in range(len(playerslist)):
        if not playerslist[i_player].is_playing():
            player_out = i_player
    if player_out != None:
        del playerslist[player_out]

print((f'The winner is {playerslist[0].get_name()}!'))