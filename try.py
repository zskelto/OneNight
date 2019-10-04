#!/usr/bin/env python3

class Werewolf:
    def __init__(self, user):
        self._role = 'werewolf'
        self._user = user
    
    def printStr(self):
        return("Role is " + self._role + " and user " + self._user)

class Medic:
    def __init__(user):
        self._role = 'medic'
        self._user = user

    def printStr(self):
        return("Role is " + self._role + " and user " + self._user)

class Seer:
    def __init__(user: str):
        self._role = 'seer'
        self._user = user

    def printStr(self):
        return("Role is " + self._role + " and user " + self._user)

class Villager:
    def __init__(user):
        self._role = 'villager'
        self._user = user

    def printStr(self):
        return("Role is " + self._role + " and user " + self._user)

class Game:
    def __init__(self, vill, wolf, medic, seer):
        self._roles = []
        self._numVill = vill
        self._numWolf = wolf
        self._numMedic = medic
        self._numSeer = seer

        for i in range(self._numVill):
            self._roles.append(Villager)
        for i in range(self._numWolf):
            self._roles.append(Werewolf)
        for i in range(self._numMedic):
            self._roles.append(Medic)
        for i in range(self._numSeer):
            self._roles.append(Seer)

        print('Setup created')
        print('---- Villagers:', self._numVill)
        print('---- Wolves   :', self._numWolf)
        print('---- Medics   :', self._numMedic)
        print('---- Seers    :', self._numSeer)

    def numPlayers(self):
        return self._numVill + self._numWolf + self._numMedic + self._numSeer

# If script being run
if __name__ == "__main__":
    import sys

    # check if valid input
    if(len(sys.argv) != 5):
        print('./try.py numVillagers numWolves numMedics numSeers')
        sys.exit(0)

    # save numbers of each role
    try:
        numVill = int(sys.argv[1])
        numWolves = int(sys.argv[2])
        numMedics = int(sys.argv[3])
        numSeers = int(sys.argv[4])
    except ValueError:
        print("Invalid input entered, make sure that all arguments are integers.")
        sys.exit(0)

    game = Game(numVill, numWolves, numMedics, numSeers)
    numPlayers = game.numPlayers()

    players = []