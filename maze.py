import sys
import os
import tkinter as tk
import random
import numpy as np

 

class Maze():
    def __init__(self):

        self.board_x = 5
        self.board_y = 5
        self.setup_board()
        sp_x, sp_y = self.calculate_allowed_start()
        self.calculate_further_path(sp_x, sp_y)
        #randoms = self.randomize_entry()
        #my_view = View(self.board_x, self.board_y, 5)#randoms)

    def setup_board(self):
        """ Generate a topographic 2dim
        matrix from the values given
        """
        self.topography = np.zeros((self.board_x, self.board_y))

 

    def calculate_allowed_start(self):
        """ From the given board size,
        return all the fields allowed as
        a starting point
        """
        random_cell_nr = random.choice(list(range(1,self.board_x -1 )))
        random_wall_nr = random.choice([1,2,3,4])

        self.update_topography(0, random_cell_nr, random_wall_nr)
 

    def update_topography(self, step, cell, wall):
        """ Update the matrix with the first value
        The value should lie at a wall but not in a corner
        """
        if wall == 1:
            #self.topography[0, cell] = 1
            sp_x, sp_y = 0, cell
        elif wall == 2:
            #self.topography[cell, self.board_y - 1] = 1
            sp_x, sp_y = cell, self.board_y - 1
        elif wall == 3:
            #self.topography[self.board_x - 1, cell] = 1
            sp_x, sp_y = self.board_x - 1, cell
        elif wall == 4:
            #self.topography[cell, 0] = 1
            sp_x, sp_y = cell, 0
        self.topography[sp_x, sp_y] = 1
        print(self.topography)
        return sp_x, sp_y


    def calculate_further_path(self, sp_x, sp_y):
        """ """
        pass

 
class View():
    def __init__(self, board_x, board_y, randoms):
        """ Initialize the general format to be displayed first """
        self.root = tk.Tk(
        self.frame = tk.Frame(self.root)
        self.board_x = board_x
        self.board_y = board_y
        self.frame.pack()

        self.draw_empty_maze(randoms)
        #self.draw_filled_maze()
        self.root.mainloop()
        self.root.destroy()

    def draw_empty_maze(self, randoms):

        for y in range(self.board_y):
            for x in range(self.board_x):
                if [x,y] == randoms:
                    rb = tk.Button(self.frame, text="o", fg = "Red")
                    rb.grid(row = y, column = x)
                else:
                    rb = tk.Button(self.frame, text="::", fg = "Black")
                    rb.grid(row = y, column = x)


my_maze = Maze()

 

 
