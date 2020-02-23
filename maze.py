import sys
import os
import itertools
import tkinter as tk
import random
import numpy as np

class Board():
    """ Define the topography for the Maze """
    def __init__(self,  board_x, board_y):
        self.board_x = board_x
        self.board_y = board_y
        self.allowed_starts = []
        # Generate a topographic 2dim matrix from the values given
        self.topography = np.zeros((self.board_x, self.board_y))
        # calculate the allowed fields for the start
        self.board_setup()


    def board_setup(self):
        """ From the given board size,
        return all the fields allowed as
        a starting point
        """
        
        for x in range(1, self.board_x - 1):
            self.allowed_starts.append([x, 0])
            self.allowed_starts.append([x, self.board_y - 1])
        for y in range(1, self.board_y - 1):
            self.allowed_starts.append([0, y])
            self.allowed_starts.append([self.board_x - 1, y])

    def remove_forbidden_fields_from_start(self):
        """ Remove fields that are neighboring the starting fields from the allowed fields variable """
        if sp_x == 0 or sp_x == board_x-1:
            try:
                print("removing {}".format([sp_x, sp_y + 1]))
                self.allowed_starts.remove([sp_x, sp_y + 1])
                print("removing {}".format([sp_x, sp_y - 1]))
                self.allowed_starts.remove([sp_x, sp_y - 1])
                
            except ValueError:
                print("Valuerror")
                pass
        elif self.sp_y == 0 or self.sp_y == self.board_y-1:
                try:
                    print("removing {}".format([sp_x + 1, sp_y]))
                    self.allowed_starts.remove([sp_x + 1, sp_y])
                    print("removing {}".format([sp_x - 1, sp_y]))
                    self.allowed_starts.remove([sp_x - 1, sp_y])
                    
                except ValueError:
                    print("Valuerror")
                    pass

    def _inside_the_board(self, x, y):
        """ Verify that the cell is inside the board """
        if x in [-1, self.board_x - 1] or y in [-1, self.board_y - 1]:
            return False
        try:
            self.topography[x, y]
            return True
        except IndexError:
            return False

class Maze():
    def __init__(self):
        """ Calculate a maze on a rectangular board """
        self.board_x = 5
        self.board_y = 5
        # define a set of forbidden cells 
        self.forbidden_cells = []
        
        self.topography = Board(self.board_x, self.board_y)

        # the maze will contain multiple paths
        self.index = 0
        # create mutiple
        while self.index < 5:
            self.calculate_allowed_start()
            if self.start_success == True:
                self.calculate_further_path(self.sp_x, self.sp_y)
            self.index += 1
        my_view = View(self.board_x, self.board_y, self.topography.topography)


    def calculate_allowed_start(self):
        """ From the given board size,
        return all the fields allowed as
        a starting point
        """
        
        print("Calculating start for path nr. {}".format(self.index))
        print("self.allowed_starts: {}".format(self.topography.allowed_starts))
        while len(self.topography.allowed_starts) > 0:
            self.sp_x, self.sp_y = random.choice(self.topography.allowed_starts)
            print("Checking neighbours for self.sp_x, self.sp_y : {}".format([self.sp_x, self.sp_y]))
            if self.check_neighbours([self.sp_x, self.sp_y], self.sp_x, self.sp_y, 0):
                print("Checked neighbours for self.sp_x, self.sp_y successfully: {}".format([self.sp_x, self.sp_y]))
                self.topography.topography[self.sp_x, self.sp_y] = 1

                self.topography.allowed_starts.remove([self.sp_x, self.sp_y])
                print("removing {}".format([self.sp_x, self.sp_y]))
                
                self.start_success = True
                break
            self.topography.allowed_starts.remove([self.sp_x, self.sp_y])
            print("removing {}".format([self.sp_x, self.sp_y]))
            self.start_success = False

    def calculate_further_path(self, sp_x, sp_y):
        """ Proceed to calculate the possible moves from the first stone"""
        possible_moves = []
        move_nr = 0
        while move_nr < 5:
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
            move_nr += 1

    def _border_not_reached(self, x, y):
        """ Verify that the cell x, y is still 
        inside the board
        """
        if x in [0, -1, self.board_x - 1] or y in [0, -1, self.board_y - 1]:
            return False
        return True

    def cell_is_ok(self, next_move_x, next_move_y, sp_x, sp_y):
        """ Check that the current cell exists inside the board 
        and does not represent the current position
        """
        current_position = [sp_x, sp_y]
        if [next_move_x, next_move_y] == current_position:
            return True
        if self.topography._inside_the_board(next_move_x, next_move_y) and self.topography.topography[next_move_x, next_move_y] != 1:
            return True
        else:
            return False
        return True
       
    def check_neighbours(self, next_move, sp_x, sp_y, start):
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
        print(self.topography.topography)
        print("possible_moves: {}".format(possible_moves))
        next_move = random.choice(possible_moves)
        print("next_move: {}".format(next_move))
        # compare with current position
        if next_move != [sp_x, sp_y]:
            
            if self.check_neighbours(next_move, sp_x, sp_y, start=0):
        
                self.topography.topography[next_move[0], next_move[1]] = 1
                return next_move[0], next_move[1]
            else:
                return sp_x, sp_y
        else:
            print("move : {} stopped, since we have been there already".format(next_move))
            return sp_x, sp_y


class View():
    def __init__(self, board_x, board_y, topography):
        """ Initialize the tk view """
        
        self.board_x = board_x
        self.board_y = board_y
        self.magnify_index = 20
        self.cell_fill_index = 18

        self.root = tk.Tk()
        self.root.title("Maze")
        self.frame = tk.Canvas(self.root, width =board_x*self.magnify_index, height=board_y*self.magnify_index, bg='grey')
        self.frame.pack()

        self.draw_maze(topography)
        self.root.mainloop()
        self.root.destroy()

    def draw_maze(self, topography):
        """ Fill the board with calculated paths
        - Iterate over all horizontal coordinates
        - Iterate over all vertical coordinates
        - Fill the cell with white/black color depending on
        the value of the matrix cell
        """
        
        for y in range(self.board_y):
            for x in range(self.board_x):
                if topography[y,x] == 1:
                    left_up_x = self.magnify_index*x
                    left_up_y = self.magnify_index*y
                    right_bot_x = self.magnify_index*x + self.cell_fill_index
                    right_bot_y = self.magnify_index*y+ self.cell_fill_index
                    self.frame.create_rectangle(left_up_x, left_up_y, right_bot_x, right_bot_y, fill = "White")

                else:
                    left_up_x = self.magnify_index*x
                    left_up_y = self.magnify_index*y
                    right_bot_x = self.magnify_index*x + self.cell_fill_index
                    right_bot_y = self.magnify_index*y+self.cell_fill_index
                    self.frame.create_rectangle(left_up_x, left_up_y, right_bot_x, right_bot_y, fill = "Black")



my_maze = Maze()

 

 
