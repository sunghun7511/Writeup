# # # -*- coding: utf-8 -*-
# # SYMBOL_EMPTY = 0
# # SYMBOL_X = 1
# # SYMBOL_FILLED = 2

 
# # def fixed_sum_digits(digits, Tot):
# #     """
# #     adapted from http://stackoverflow.com/a/8617750

# #     Given digits and Tot, it generates an array of all ways to arrange "digits" x digits so that
# #     the sum of them is "Tot". Zero can be a digit on either end, otherwise it must be one or greater
# #     """
# #     ways = []

# #     def iter_fun(sum, deepness, sequence, Total):
# #         if deepness == 0:
# #             if sum == Total:
# #                 ways.append(sequence)
# #         else:
# #             on_end = deepness == 1 or deepness == digits
# #             for i in range(0 if on_end else 1, Total - sum + 1):
# #                 iter_fun(sum + i, deepness - 1, sequence + [i], Total) 

# #     iter_fun(0, digits, [], Tot) 
# #     return ways


# # def generate_possible_rows(nums, size):
# #     digits = len(nums) + 1
# #     space_left = size - sum(nums)
# #     combos = fixed_sum_digits(digits, space_left)

# #     rows = []
# #     for combo in combos:
# #         row = [None] * (len(combo) + len(nums))
# #         row[::2] = combo
# #         row[1::2] = nums
# #         out = []
# #         curr = SYMBOL_X
# #         for r in row:
# #             out.extend([curr] * r)
# #             curr = SYMBOL_X if (curr == SYMBOL_FILLED) else SYMBOL_FILLED
# #         rows.append(out)
# #     return rows


# # def filter_rows(rows, existing):
# #     def is_row_okay(row, existing):
# #         for i in range(0, len(existing)):
# #             if existing[i] != 0 and row[i] != existing[i]:
# #                 return False
# #         return True
# #     return [row for row in rows if is_row_okay(row, existing)]


# # def find_common_rows(rows, size):
# #     row_x = [SYMBOL_X] * size
# #     row_filled = [SYMBOL_FILLED] * size

# #     for row in rows:
# #         for i in range(0, size):
# #             if row[i] == SYMBOL_FILLED:
# #                 row_x[i] = SYMBOL_EMPTY
# #             if row[i] == SYMBOL_X:
# #                 row_filled[i] = SYMBOL_EMPTY

# #     return [x + y for x, y in zip(row_x, row_filled)]


# # def do_row(nums, size, existing=None):
# #     possible = generate_possible_rows(nums, size)

# #     if existing is not None:
# #         possible = filter_rows(possible, existing)

# #     common = find_common_rows(possible, size)

# #     if existing is not None:
# #         for i in range(0, size):
# #             if common[i] == SYMBOL_EMPTY:
# #                 common[i] = existing[i]

# #     return common


# # def is_row_filled(row):
# #     for x in row:
# #         if x == SYMBOL_EMPTY:
# #             return False
# #     return True


# # # Grid abstraction handlers
# # def grid_make(w, h):
# #     return [[SYMBOL_EMPTY for i in range(0, w)] for j in range(0, h)]
# # def grid_get_row(grid, row):
# #     return grid[row]
# # def grid_get_col(grid, col):
# #     return [row[col] for row in grid]
# # def grid_set_row(grid, row, val):
# #     grid[row] = val
# # def grid_set_col(grid, col, val):
# #     for row in range(0, len(grid)):
# #         grid[row][col] = val[row]
# # def grid_print(grid):
# #     symbol_print = [' ', '·', '█']
# #     for row in grid:
# #         s = ""
# #         for x in row:
# #             s += symbol_print[x]
# #         print(s)
# # def grid_filled(grid):
# #     for row in grid:
# #         if not is_row_filled(row):
# #             return False
# #     return True

# # def go(cols, rows):
# #     w = len(cols)
# #     h = len(rows)
# #     g = grid_make(w, h)

# #     while not grid_filled(g):
# #         for i in range(0, h):
# #             row = grid_get_row(g, i)
# #             if is_row_filled(row):
# #                 continue

# #             d = do_row(rows[i], h, row)
# #             grid_set_row(g, i, d)


# #         for i in range(0, w):
# #             col = grid_get_col(g, i)
# #             if is_row_filled(col):
# #                 continue

# #             d = do_row(cols[i], w, col)
# #         # grid_print(g)
# #     return g


# from itertools import izip
 
# def gen_row(w, s):
#     """Create all patterns of a row or col that match given runs."""
#     def gen_seg(o, sp):
#         if not o:
#             return [[2] * sp]
#         return [[2] * x + o[0] + tail
#                 for x in xrange(1, sp - len(o) + 2)
#                 for tail in gen_seg(o[1:], sp - x)]
 
#     return [x[1:] for x in gen_seg([[1] * i for i in s], w + 1 - sum(s))]
 
 
# def deduce(hr, vr):
#     """Fix inevitable value of cells, and propagate."""
#     def allowable(row):
#         print(row)
#         return reduce(lambda x, y: [a | b for a, b in izip(x, y)], row)
 
#     def fits(a, b):
#         return all(x & y for x, y in izip(a, b))
 
#     def fix_col(n):
#         """See if any value in a given column is fixed;
#         if so, mark its corresponding row for future fixup."""
#         c = [x[n] for x in can_do]
#         cols[n] = [x for x in cols[n] if fits(x, c)]
#         for i, x in enumerate(allowable(cols[n])):
#             if x != can_do[i][n]:
#                 mod_rows.add(i)
#                 can_do[i][n] &= x
 
#     def fix_row(n):
#         """Ditto, for rows."""
#         c = can_do[n]
#         rows[n] = [x for x in rows[n] if fits(x, c)]
#         for i, x in enumerate(allowable(rows[n])):
#             if x != can_do[n][i]:
#                 mod_cols.add(i)
#                 can_do[n][i] &= x
 
#     def show_gram(m):
#         # If there's 'x', something is wrong.
#         # If there's '?', needs more work.
#         for x in m:
#             print " ".join("x#.?"[i] for i in x)
#         print
 
#     w, h = len(vr), len(hr)
#     rows = [gen_row(w, x) for x in hr]
#     cols = [gen_row(h, x) for x in vr]
#     can_do = map(allowable, rows)
 
#     # Initially mark all columns for update.
#     mod_rows, mod_cols = set(), set(xrange(w))
 
#     while mod_cols:
#         for i in mod_cols:
#             fix_col(i)
#         mod_cols = set()
#         for i in mod_rows:
#             fix_row(i)
#         mod_rows = set()
 
#     if all(can_do[i][j] in (1, 2) for j in xrange(w) for i in xrange(h)):
#         print "Solution would be unique" # but could be incorrect!
#     else:
#         print "Solution may not be unique, doing exhaustive search:"
 
#     # We actually do exhaustive search anyway. Unique solution takes
#     # no time in this phase anyway, but just in case there's no
#     # solution (could happen?).
#     out = [0] * h
 
#     def try_all(n = 0):
#         if n >= h:
#             for j in xrange(w):
#                 if [x[j] for x in out] not in cols[j]:
#                     return 0
#             show_gram(out)
#             return 1
#         sol = 0
#         for x in rows[n]:
#             out[n] = x
#             sol += try_all(n + 1)
#         return sol
 
#     n = try_all()
#     if not n:
#         print "No solution."
#     elif n == 1:
#         print "Unique solution."
#     else:
#         print n, "solutions."
#     print


import sys
import string
import copy
import types
from data_diff import data_diff

def get_permutations(counts, length):
    if len(counts) == 0:
        row = []
        for x in xrange(length):
            row.append(False)
        return [row]

    permutations = []
    
    for start in xrange(length - counts[0] + 1):
        permutation = []
        for x in xrange(start):
            permutation.append(False)
        for x in xrange(start, start + counts[0]):
            permutation.append(True)
        x = start + counts[0]
        if x < length:
            permutation.append(False)
            x += 1
        if x == length and len(counts) == 0:
            permutations.append(permutation)
            break
        sub_start = x
        sub_rows = get_permutations(counts[1:len(counts)], length - sub_start)
        for sub_row in sub_rows:
            sub_permutation = copy.deepcopy(permutation)
            for x in xrange(sub_start, length):
                sub_permutation.append(sub_row[x-sub_start])
            permutations.append(sub_permutation)
    return permutations

def solve_row(counts, row):
    permutations = get_permutations(counts, len(row))
    valid_permutations = []
    for permutation in permutations:
        valid = True
        for x in xrange(len(row)):
            if row[x] != None and row[x] != permutation[x]:
                valid = False
        if valid:
            valid_permutations.append(permutation)

    new_row = copy.deepcopy(valid_permutations[0])
    for permutation in valid_permutations:
        for x in xrange(len(row)):
            if new_row[x] != permutation[x]:
                new_row[x] = None
        
    return new_row

def solve(row_counts, col_counts, grid):
    width = len(grid[0])
    height = len(grid)
    
    changed = True
    while changed:
        changed = False
        for x in xrange(width):
            col = []
            for y in xrange(height):
                col.append(grid[y][x])
            col = solve_row(col_counts[x], col)
            for y in xrange(height):
                if col[y] != None and grid[y][x] != col[y]:
                    changed = True
                grid[y][x] = col[y]
                
        for y in xrange(height):
            row = copy.deepcopy(grid[y])
            row = solve_row(row_counts[y], row)
            for x in xrange(width):
                if row[x] != None and grid[y][x] != row[x]:
                    changed = True
            grid[y] = row
        
    return grid

def check_solution(grid):
    row_counts = []
    col_counts = []
    
    for y in xrange(len(grid)):
        row_counts.append([0])
    for x in xrange(len(grid[0])):
        col_counts.append([0])
    
    for y in xrange(len(grid)):
        for x in xrange(len(grid[0])):
            if grid[y][x] == True:
                row_counts[y][-1] += 1
                col_counts[x][-1] += 1
            elif grid[y][x] == False:
                if row_counts[y][-1] != 0:
                    row_counts[y].append(0)
                if col_counts[x][-1] != 0:
                    col_counts[x].append(0)
    
    for y in xrange(len(grid)):
        if row_counts[y][-1] == 0:
            row_counts[y].pop()
    for x in xrange(len(grid[0])):
        if col_counts[x][-1] == 0:
            col_counts[x].pop()
    
    return [row_counts, col_counts]

def solve_from_file(filename):
    f = open(filename)

    lines = f.readlines()

    #convert into a list of lists and remove whitespace
    grid = []
    width = 0
    for line in lines:
        line = line.rstrip()
        if line:
            row = string.split(line, "\t")
            width = max(width, len(row))
            grid.append(row)
    height = len(grid)
    
    #convert into integers and normalize row width
    y = 0
    for row in grid:
        new_row = []
        for x in xrange(width):
            try:
                i = int(row[x])
            except IndexError:
                i = None
            except ValueError:
                if row[x] == 'T':
                    i = True
                elif row[x] == 'F':
                    i = False
                else:
                    i = None            
            new_row.append(i)
        grid[y] = new_row
        y += 1

    #measure height and width of inner grid
    x = width - 1
    y = height - 1
    while x >= 0:
        if type(grid[y][x]) == types.IntType:
            break
        x -= 1
    inner_width = width - x - 1

    x = width - 1
    y = height - 1
    while y >= 0:
        if type(grid[y][x]) == types.IntType:
            break
        y -= 1
    inner_height = len(grid) - y - 1

    print "board size: %dx%d" % (inner_width, inner_height)

    #ensure inner grid is valid
    for x in xrange(width - inner_width, width):
        for y in xrange(height - inner_height, height):
            if type(grid[y][x]) != types.NoneType and type(grid[y][x]) != types.BooleanType:
                print 'invalid board'
                exit()
                
    #ensure upper left is empty
    for x in xrange(width - inner_width):
        for y in xrange(height - inner_height):
            if grid[y][x] != None:
                print 'invalid board'
                exit()

    counts_width = width - inner_width
    counts_height = height - inner_height

    #populate row counts
    row_counts = []
    for y in xrange(counts_height, height):
        counts = []
        for x in xrange(counts_width):
            count = grid[y][x]
            if count:
                counts.append(count)
        row_counts.append(counts)

    #populate column counts
    col_counts = []
    for x in xrange(counts_width, width):
        counts = []
        for y in xrange(counts_height):
            count = grid[y][x]
            if count:
                counts.append(count)
        col_counts.append(counts)

    #redo grid
    width = inner_width
    height = inner_height
    inner_grid = []
    for y in xrange(height):
        inner_grid.append([])
        for x in xrange(width):
            inner_grid[y].append(grid[y+counts_height][x+counts_width])

    grid = solve(row_counts, col_counts, inner_grid)

    complete = True
    for row in grid:
        for item in row:
            if item == None:
                complete = False

    if complete:
        l = check_solution(grid)
        if data_diff(l[0], row_counts) or data_diff(l[1], col_counts):
            print 'FAIL!'
            exit()

    for y in xrange(counts_height):
        for x in xrange(counts_width):
            sys.stdout.write("\t")
        for counts in col_counts:
            try:
                sys.stdout.write(str(counts[-counts_height+y]))
            except:
                pass
            sys.stdout.write("\t")
        print
    y = 0
    for row in grid:
        for x in xrange(counts_width):
            try:
                sys.stdout.write(str(row_counts[y][-counts_width+x]))
            except:
                pass
            sys.stdout.write("\t")
        for square in row:
            if square == True:
                sys.stdout.write('T')
            elif square == False:
                sys.stdout.write('F')
            sys.stdout.write("\t")
        print
        y += 1
        