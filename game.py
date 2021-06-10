import numpy as np

score = np.zeros([3, 3])
result = False
gameEnded =0
iteration = 0

class game():
   #Initiate Class with empty board
   def __init__(self):
      self.cells = np.full(9," ", dtype= str)
   #Add a play
   def play(self, player, entry):
         self.cells[entry-1] = player
   #Display current status
   def show(self):
      print("|| %s || %s || %s ||" %(self.cells[0], self.cells[1], self.cells[2]))
      print("|| %s || %s || %s ||" %(self.cells[3], self.cells[4], self.cells[5]))
      print("|| %s || %s || %s ||" %(self.cells[6], self.cells[7], self.cells[8]))
   #Check if gmae has ended
   def CheckResult(self):
      cells = np.array(self.cells)
      cells= cells.reshape(3,3)
      for x in range(3):
         for y in range(3):
            if cells[x, y] == "X":
               score[x, y] = 1
            elif cells[x, y]=="O":
               score[x, y] = -1

      if 3 in np.sum(score, axis=0):    
         return True, "X"
      elif 3 in np.sum(score,axis=1):
         return True, "X"
      elif np.trace(score)==3 or np.sum(np.diag(np.rot90(score)))==3:
         return True, "X"
      elif -3 in np.sum(score, axis=0):
         return True, "O"
      elif -3 in np.sum(score,axis=1):
         return True, "O"
      elif np.trace(score)==-3 or np.sum(np.diag(np.rot90(score)))==-3:
         return True, "O"
      else:
         return False, "Noone"
               
#Initiate game
board = game()

#Play loop
while gameEnded == False:

   if (iteration%2==1):
      player = "X"
   else:
      player = "O"

   print("Now playing "+ player) 

   board.play(player, int(input('Enter Position : ')))

   gameEnded, winner = board.CheckResult()

   if gameEnded == True:
      print('Player '+winner+ " won!!")

   board.show()

   iteration+=1