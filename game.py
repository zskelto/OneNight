class Player:
    username = " "
    team = " "
    role = " "
    action = " "

    def __init__(self, n, r):
        self.username = n
        self.role = role

#Determines the Player Base.
Players=0
Deck=0
Werewolves=0
Towns=0
#Specify What Roles to Include.
#Tanner
Tanner=0
#Werewolves
Alpha=0
Mystic=0
Minion=0
#Townies
Paranormal_Investigator=0
Aura_Seer=0
Robber=0
Troublemaker=0
Witch=0
Drunk=0
Doppelganger=0

#Determines the number of players
Players = input("How many players?\n")
while Players<3:
    print "There should be at least 3 players for a game."
    Players=input("Please enter the amount of players:\n")

#Makes the teams
Deck = Players+3
Werewolves=Deck/3
Towns=Deck-Werewolves
print ("There are " + str(Werewolves) + " Werewolves and " + str(Towns) + " Villagers\n")


