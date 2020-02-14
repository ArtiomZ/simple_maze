import sys
import os
import tkinter as tk
import random
import numpy as np

 

class Maze():
    def __init__(self):

        self.board_x = 35
        self.board_y = 35
        self.setup_board()
        self.calculate_allowed_start()
        self.calculate_further_path(self.sp_x, self.sp_y)
        #randoms = self.randomize_entry()
        my_view = View(self.board_x, self.board_y, self.topography)#randoms)

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

        self.sp_x, self.sp_y = self.update_topography(0, random_cell_nr, random_wall_nr)
 

    def update_topography(self, step, cell, wall):
        """ Update the matrix with the first value
        The value should lie at a wall but not in a corner
        """
        if wall == 1:
            sp_x, sp_y = 0, cell
        elif wall == 2:
            sp_x, sp_y = cell, self.board_y - 1
        elif wall == 3:
            sp_x, sp_y = self.board_x - 1, cell
        elif wall == 4:
            sp_x, sp_y = cell, 0
        self.topography[sp_x, sp_y] = 1
        print(self.topography)
        return sp_x, sp_y


    def calculate_further_path(self, sp_x, sp_y):
        """ Proceed to calculate the possible moves from the first stone"""
        possible_moves = []
        a = 0
        while a < 55:
            possible_moves = []
            # which directions can we move from here?
            if self._border_not_reached(sp_x + 1, sp_y):
                print("no border at {},{}".format(str(sp_x + 1), str(sp_y)))
                print("we can move left")
                possible_moves.append([sp_x + 1, sp_y])
            if self._border_not_reached(sp_x - 1, sp_y):
                print("no border at {},{}".format(str(sp_x - 1), str(sp_y)))
                print("we can move left")
                possible_moves.append([sp_x - 1, sp_y])
            if self._border_not_reached(sp_x, sp_y +1):
                print("no border at {},{}".format(str(sp_x), str(sp_y + 1)))
                print("we can move down")
                possible_moves.append([sp_x, sp_y +1])
            if self._border_not_reached(sp_x, sp_y -1):
                print("no border at {},{}".format(str(sp_x), str(sp_y - 1)))
                print("we can move up")
                possible_moves.append([sp_x, sp_y -1])
            print(possible_moves)
            sp_x, sp_y = self.decide_on_move(possible_moves)
            a += 1

    def _border_not_reached(self, x, y):
        """ Verify that the cell x, y is still 
        inside the board
        """
        try:
            self.topography[x,y]
        except IndexError:
            return False
        return True

    def decide_on_move(self, possible_moves):
        """ Take a random move """
        next_move = random.choice(possible_moves)
        print(next_move)
        print(next_move[0])
        print(next_move[1])
        self.topography[next_move[0], next_move[1]] = 1
        return next_move[0], next_move[1]


class View():
    def __init__(self, board_x, board_y, topography):
        """ Initialize the general format to be displayed first """
        
        self.board_x = board_x
        self.board_y = board_y
        self.root = tk.Tk()
        self.root.title("Maze")
        self.frame = tk.Canvas(self.root, width =board_x*20, height=board_y*20, bg='grey')

        self.frame.pack()

        self.draw_empty_maze(topography)
        #self.draw_filled_maze()
        self.root.mainloop()
        self.root.destroy()

    def draw_empty_maze(self, topography):

        for y in range(self.board_y):
            for x in range(self.board_x):
                if topography[x,y] == 1:
                    left_up_x = 20*x
                    left_up_y = 20*y
                    right_bot_x = 20*x + 18
                    right_bot_y = 20*y+ 18
                    self.frame.create_rectangle(left_up_x,left_up_y, right_bot_x, right_bot_y, fill = "White")
                    #rb = tk.Button(self.frame, text="o", fg = "Red")
                    #rb.grid(row = y, column = x)
                else:
                    left_up_x = 20*x
                    left_up_y = 20*y
                    right_bot_x = 20*x + 18
                    right_bot_y = 20*y+18
                    self.frame.create_rectangle(left_up_x,left_up_y, right_bot_x, right_bot_y, fill = "Black")
                    #rb = tk.Button(self.frame, text="::", fg = "Black")
                    #rb.grid(row = y, column = x)


my_maze = Maze()

 

 
