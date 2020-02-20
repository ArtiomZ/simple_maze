import sys
import os
import tkinter as tk
import random
import numpy as np

 

class Maze():
    def __init__(self):

        self.board_x = 10
        self.board_y = 10
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
        while a < 5:
            possible_moves = []
            # which directions can we move from here?
            if self._border_not_reached(sp_x + 1, sp_y):
                possible_moves.append([sp_x + 1, sp_y])
            if self._border_not_reached(sp_x - 1, sp_y):
                possible_moves.append([sp_x - 1, sp_y])
            if self._border_not_reached(sp_x, sp_y +1):
                possible_moves.append([sp_x, sp_y +1])
            if self._border_not_reached(sp_x, sp_y -1):
                possible_moves.append([sp_x, sp_y -1])
            print(possible_moves)
            sp_x, sp_y = self.decide_on_move(possible_moves, sp_x, sp_y)
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

    def check_current_position(self, next_move, sp_x, sp_y):
        """ Verify that the new position is not the one
        where we have been before
        """
        return next_move != [sp_x, sp_y]

    def cell_is_ok(self, next_move_x, next_move_y, sp_x, sp_y):
        """ Check that the current cell exists inside the board 
        and does not represent the current position
        """
        current_position = [sp_x, sp_y]
        if [next_move_x, next_move_y] == current_position:
            return False
        try:
            if self.topography[next_move_x, next_move_y] == 1:
                return False
        except IndexError:
            return False

        return 
       
    def check_neighbours(self, next_move, sp_x, sp_y):
        """ Verify that the neighbours are not taken yet """
        if not self.cell_is_ok(next_move[0] + 1, next_move[1], sp_x, sp_y):
            return False
        elif not self.cell_is_ok(next_move[0], next_move[1] + 1, sp_x, sp_y):
            return False
        elif not self.cell_is_ok(next_move[0] - 1, next_move[1], sp_x, sp_y):
            return False
        elif not self.cell_is_ok(next_move[0], next_move[1] - 1, sp_x, sp_y):
            return False
        else: 
            return True

    def decide_on_move(self, possible_moves, sp_x, sp_y):
        """ Take a random move """
        print(possible_moves)
        next_move = random.choice(possible_moves)
        print(next_move)
        print(next_move[0])
        print(next_move[1])
        if self.check_current_position(next_move, sp_x, sp_y):
            print(self.topography)
            if self.check_neighbours(next_move, sp_x, sp_y):
        
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

 

 
