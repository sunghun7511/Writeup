# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw

SYMBOL_EMPTY = 0
SYMBOL_X = 1
SYMBOL_FILLED = 2

# 
def fixed_sum_digits(digits, Tot):
    """
    adapted from http://stackoverflow.com/a/8617750

    Given digits and Tot, it generates an array of all ways to arrange "digits" x digits so that
    the sum of them is "Tot". Zero can be a digit on either end, otherwise it must be one or greater
    """
    ways = []
    def iter_fun(sum, deepness, sequence, Total):
        if deepness == 0:
            if sum == Total:
                ways.append(sequence)
        else:
            on_end = deepness == 1 or deepness == digits
            for i in range(0 if on_end else 1, Total - sum + 1):
                iter_fun(sum + i, deepness - 1, sequence + [i], Total) 

    iter_fun(0, digits, [], Tot) 
    return ways


def generate_possible_rows(nums, size):     
    digits = len(nums) + 1
    space_left = size - sum(nums)
    combos = fixed_sum_digits(digits, space_left)

    rows = []
    for combo in combos:
        row = [None] * (len(combo) + len(nums))
        row[::2] = combo
        row[1::2] = nums
        out = []
        curr = SYMBOL_X;
        for r in row:
            out.extend([curr] * r)
            curr = SYMBOL_X if (curr == SYMBOL_FILLED) else SYMBOL_FILLED
        rows.append(out)
    return rows

def filter_rows(rows, existing):
    def is_row_okay(row, existing):
        for i in range(0, len(existing)):
            if existing[i] != 0 and row[i] != existing[i]:
                return False
        return True
    return [row for row in rows if is_row_okay(row, existing)]

def find_common_rows(rows, size):
    row_x = [SYMBOL_X] * size
    row_filled = [SYMBOL_FILLED] * size

    for row in rows:
        for i in range(0, size):
            if row[i] == SYMBOL_FILLED:
                row_x[i] = SYMBOL_EMPTY
            if row[i] == SYMBOL_X:
                row_filled[i] = SYMBOL_EMPTY

    return [x + y for x, y in zip(row_x, row_filled)]

def do_row(nums, size, existing=None):
    possible = generate_possible_rows(nums, size)

    if existing is not None:
        possible = filter_rows(possible, existing)

    common = find_common_rows(possible, size)

    if existing is not None:
        for i in range(0, size):
            if common[i] == SYMBOL_EMPTY:
                common[i] = existing[i]

    return common

def is_row_filled(row):
    for x in row:
        if x == SYMBOL_EMPTY:
            return False
    return True


# Grid abstraction handlers
def grid_make(w, h):
    return [[SYMBOL_EMPTY for i in range(0, w)] for j in range(0, h)]
def grid_get_row(grid, row):
    return grid[row]
def grid_get_col(grid, col):
    return [row[col] for row in grid]
def grid_set_row(grid, row, val):
    grid[row] = val
def grid_set_col(grid, col, val):
    for row in range(0, len(grid)):
        grid[row][col] = val[row]
def grid_print(grid):
    symbol_print = [' ', '·', '█']
    for row in grid:
        s = ""
        for x in row:
            s += symbol_print[x]
        print(s)
def grid_filled(grid):
    for row in grid:
        if not is_row_filled(row):
            return False
    return True
def grid_image(grid, size=10):
    w, h = len(grid[0]), len(grid)
    im = Image.new("RGB", (w * size, h * size), (255, 255, 255))
    draw = ImageDraw.Draw(im)

    for y in range(0, h):
        row = grid[y]
        for x in range(0, w):
            val = row[x]
            coord = [(x * size, y * size), ((x + 1) * size, (y + 1) * size)]

            if val == SYMBOL_FILLED:
                draw.rectangle(coord, fill=(0, 0, 0))
            if val == SYMBOL_X:
                draw.rectangle(coord, fill=(255, 128, 128))
    return im
# end grid abstraction handlers

def go(cols, rows):
    w = len(cols)
    h = len(rows)
    g = grid_make(w, h)
    num = 0
    def snapshot(name="nonogram"):
        nonlocal num
        im = grid_image(g)
        im.save("%s_%04d.png" % (name, num))
        num += 1

    snapshot()
    while not grid_filled(g):
        for i in range(0, h):
            row = grid_get_row(g, i)
            if is_row_filled(row):
                continue

            d = do_row(test_rows[i], h, row)
            grid_set_row(g, i, d)
            # snapshot()

        for i in range(0, w):
            col = grid_get_col(g, i)
            if is_row_filled(col):
                continue

            d = do_row(test_cols[i], w, col)
            grid_set_col(g, i, d)
            # snapshot()
    snapshot()
    return g



# test stuff
#test_cols = [(2, 2, 5), (2, 1, 9), (3, 4, 3), (3, 3, 2, 1), (3, 3, 5, 2), (4, 2, 3, 2), (9, 2), (9, ), (16, ), (1, 15), (1, 11, 3), (14, 2), (2, 6, 5, 2), (1, 7, 2, 2), (1, 9, 4), (11, 2), (10, 2), (10, 1, 2), (8, 1, 2), (5, 3)]
#test_rows = [(2,), (4, 4), (1, 3, 1, 5), (3, 1, 2, 3), (1, 3, 4, 5), (2, 14), (15,), (14,), (16,), (18,), (4, 14), (3, 7, 6), (3, 9, 4), (2, 2, 6), (2, 2, 2, 4, 2), (2, 2, 1, 2, 4, 1), (2, 3, 2, 1, 3, 1), (2, 1, 3, 2, 4), (2, 1, 5, 2), (3, 3)]

#test_rows = [(2,2,11),(3,4,13),(3,5,11),(4,3,10),(3,3,3,1),(1,1,1,1,1,1),(5,3,4),(1,1,4,2,5,1),(3,2,2,5),(1,2,3,3,1),(1,6,1,1,1),(1,4,1,1,2),(5,4,5,1),(10,1,3,5),(8,1,1,8,2),(11,5,9),(1,3,5,9),(1,1,1,1,5,7),(3,6,8),(21,),(3,2,9,10),(6,4,3,5,1),(6,5),(3,5),(3,2,6),(3,5,1,1,3),(5,3,4,1,1,4),(3,2,3,6),(3,3,1,9),(2,2,1,2,4)]
#test_cols = [(2,4,1,3,3,4),(2,1,1,1,1,3,4),(3,3,7,5,3),(3,1,5,4,1),(6,6,4,1),(1,2,4,3),(3,4,1,1,2),(2,3,1,2),(3,3,3,1),(5,3,3,2),(4,1,1,4,1),(4,1,1,5),(1,1,3,3,1,1),(7,4,1,3),(1,14,2),(1,1,3,7,2),(4,1,9,2),(6,1,1,7,1),(5,1,7),(6,1,1,9),(4,1,1,6,1,1),(4,4,18),(4,3,13,1),(5,23),(3,3,8,5),(3,16,4),(3,1,6,4),(1,1,8,3),(1,3,3,3),(1,1,1,2,1,2)]

test_rows = [[1, 3, 7, 5], [1, 3, 2, 5, 1, 3], [4, 1, 3, 4, 2], [5, 1, 2, 4, 3], [1, 5, 1, 2, 1, 3], [3, 2, 2, 2, 1, 2], [6, 11], [3, 1, 1, 1, 2, 1, 4], [2, 4, 6, 4], [3, 3, 2, 3, 1, 1], [2, 5, 3, 1, 1], [1, 3, 6, 3, 2], [3, 3, 4, 1, 1, 2], [5, 7, 3], [2, 2, 1, 1, 6], [2, 2, 4, 1, 5], [1, 10, 6], [2, 10, 4], [6, 6, 1, 3]]
test_cols = [[4, 1, 3, 3], [6, 3, 9], [7, 1, 7, 2], [1, 5, 1, 3, 3, 1], [2, 6, 1, 2, 3], [1, 1, 1, 4, 1, 2], [2, 6], [2, 1, 1, 1, 2, 1, 2], [4, 4, 3, 5], [5, 0, 3], [2, 2, 4], [5, 4, 2, 2, 1], [5, 2, 1, 1, 2], [3, 1, 2], [5, 1, 2, 1, 1, 1], [4, 3, 0], [1, 1, 1, 2, 7], [9], [2, 4, 4, 2]]

# test_rows = [(7,),(3,3),(1,2),(3,3,2),(1,1,1,1,2),(1,1,1,1),(1,1,1,1,1,1), (1,1,1,1,2),(2,1,2,1,1),(7,4,1,1),(1,1,1,1,1,2,1),(3,1,11,1),(16,1),(14,2),(4,1,1),(4,2,1,2),(1,2,1,1,2),(2,2,1,3),(1,1,4),(5,)]
# test_cols = [(4,4),(2,2,3,1),(1,1,5,1,1),(2,1,6),(1,10),(1,2,1,4),(1,1,1,6),(2,2,2,3,3),(1,4,3,2,1),(1,3,1,2),(1,4,1,1,1),(1,3,1,4,1,2),(1,2,3,1,1),(2,1,3,1),(1,1,2,2),(2,2,1),(2,2,2),(2,2,2),(4,3),(7,)]

go(test_cols, test_rows)

# remove duplicates with
# fdupes -rdN .
# turn it into a gif with
# convert -delay 10 -loop 0 nonogram*.png anim.gif