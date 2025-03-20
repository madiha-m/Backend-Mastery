# Create parent class
class Player:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

# Child class


class NewPlayer(Player):
    def __init__(self, fname, lname, total):
        Player.__init__(self, fname, lname)
        self.total = total

    def getDetails(self):
        return '%s %s has spent %s in total.' % (self.fname, self.lname, self.total)


new_player = NewPlayer('madiha', 'Muhammad', 10000)
print(new_player.getDetails())
