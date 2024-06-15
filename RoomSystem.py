class Room:
    def __init__(self):
        self.players = []

    def PlayerConnected(self, Player: str):
        return self.players.append(Player)
    
    def Is_empty(self):
        return len(self.players) == 0

    def DesconectPlayer(self):
        if not self.Is_empty():
            return self.players.pop(0)
        else:
            return None

    def PlayerList(self):
        for Player in self.players:
            print(Player)


NewRoom = Room()
NewRoom.PlayerConnected('Neptune')

#print(NewRoom.players[0])
#NewRoom.RemovePlayer()
#print(NewRoom.players[0])

#NewRoom.AddPlayer('Neptune')
NewRoom.PlayerConnected('Poggers123')
NewRoom.PlayerConnected('PvPGuy')
NewRoom.PlayerConnected('TheProPlayer52')

NewRoom.PlayerList()
