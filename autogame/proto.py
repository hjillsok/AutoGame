from random import randint

class Room:
    def __init__(self,NAME,coords):
        self.name = NAME
        self.row = coords[0]
        self.col = coords[1]
        self.floor = coords[2]
        self.neighbors = {}
        self.exits = {}
    
    def addNeighbor(self,end,direction):
        self.neighbors[direction] = end
    
    def addExit(self,end,direction):
        self.exits[direction] = end
    
class Dungeon:
    def __init__(self,rows,cols,floors):
        self.rooms = {}
        self.rows = rows
        self.cols = cols
        self.floors = floors
        self.generate(rows,cols,floors)
        self.start = ""
        
    def travel(self,end):
        pass
    
    def generate(self,rows,cols,floors):
        for z in range(1,floors):
            for y in range(1,cols):
                for x in range(1,rows):
                    n = "Room {},{},{}".format(x,y,z)
                    self.rooms[n] = Room(n,(x,y,z))
        for room in self.rooms:
            row = room.row
            col = room.col
            flo = room.flo
            if row > 1:
                neigh = "Room {},{},{}".format(row - 1,col,flo)
                self.addNeighbor(room,self.rooms[neigh],"West")
            if row < self.rows:
                neigh = "Room {},{},{}".format(row + 1,col,flo)
                self.addNeighbor(room,self.rooms[neigh],"East")
            if col > 1:
                neigh = "Room {},{},{}".format(row,col-1,flo)
                self.addNeighbor(room,self.rooms[neigh],"North")
            if col < self.cols:
                neigh = "Room {},{},{}".format(row,col + 1,flo)
                self.addNeighbor(room,self.rooms[neigh],"South")
            if flo > 1:
                neigh = "Room {},{},{}".format(row,col,flo - 1)
                self.addNeighbor(room,self.rooms[neigh],"Down")
            if flo < self.floors:
                neigh = "Room {},{},{}".format(row,col,flo + 1)
                self.addNeighbor(room,self.rooms[neigh],"Up")
                
        x = randint(1,self.rows)
        y = randint(1,self.cols)
        z = randint(1,self.floors)
        self.start = self.rooms["Room {},{},{}".format(x,y,z)]
        
    def addNeighbor(self,start,end,direction):
        start.addNeighbor(end,direction)
        if direction == "North":
            end.addNeighbor(start,"South")
        if direction == "South":
            end.addNeighbor(start,"North")
        if direction == "East":
            end.addNeighbor(start,"West")
        if direction == "West":
            end.addNeighbor(start,"East")
        if direction == "Up":
            end.addNeighbor(start,"Down")
        if direction == "Down":
            end.addNeighbor(start,"Up")
