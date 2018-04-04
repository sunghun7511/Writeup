# -*- coding: utf-8 -*-

import sys
from termcolor import colored
from nonogram.solvers import SimpleSolver


class PuzzleError(Exception):
    pass


class Puzzle:
    verticals = [[]]
    horizontals = [[]]
    board = [[]]
    solvers = []

    spacer_offset_y = 0
    spacer_distance_y = 5
    spacer_offset_x = 0
    spacer_distance_x = 5

    def __init__(self, verticals, horizontals):
        self.verticals = verticals
        self.horizontals = horizontals
        self.make_board(len(verticals), len(horizontals))
        self.check_consistency()
        self.solvers = [SimpleSolver(self)]

    def make_board(self, width, height):
        """Initializes the board in the board instance variable with the given width and height."""

        self.board = [[None] * width for _ in range(height)]

    def check_consistency(self):
        # Check if amount of values in rows matches amounts in columns
        if sum(sum(self.verticals, [])) != sum(sum(self.horizontals, [])):
            raise PuzzleError("Sums of verticals and horizontals don't match")

        # Check if all columns and rows can fit
        for i, h in enumerate(self.horizontals):
            if sum(h) + len(h) - 1 > len(self.verticals):
                raise PuzzleError("Row {} can't possibly fit".format(i))
        for i, v in enumerate(self.verticals):
            if sum(v) + len(v) - 1 > len(self.horizontals):
                raise PuzzleError("Column {} can't possibly fit".format(i))

    def solve(self):
        while self.solve_step():
            continue

    def solve_step(self):
        for s in self.solvers:
            if s.solve_step():
                return True
        return False

    def printt(self, show_diff_with=None):
        """Prints the board to stdout"""

        for i, row in enumerate(self.board):
            # Draw 5x5 grid
            if i % self.spacer_distance_y == self.spacer_offset_y and i > 0:
                for j in range(len(row)):
                    if j % self.spacer_distance_x == self.spacer_offset_x and j > 0:
                        sys.stdout.write("┼")
                    sys.stdout.write("──")
                sys.stdout.write("\n")

            for j, column in enumerate(row):
                # Draw 5x5 grid
                if j % self.spacer_distance_x == self.spacer_offset_x and j > 0:
                    sys.stdout.write("│")

                if column is None:
                    to_write = "░░"
                elif not column:
                    to_write = "  "
                else:
                    to_write = "█▊"

                if show_diff_with and show_diff_with[i][j] != column:
                    sys.stdout.write(colored(to_write, on_color='on_red', attrs=['bold']))
                else:
                    sys.stdout.write(to_write)
            sys.stdout.write("\n")