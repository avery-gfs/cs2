# Print a bar chart based on the numbers in the list `numbers` where each number
# `n` in the list gets its own column with `n` `X` characters in it.
#
# For the numbers (1, 4, 2, 7, 3) the output should be:
#
#    X
#    X
#    X
#  X X
#  X XX
#  XXXX
# XXXXX

l = [1, 4, 2, 7, 3]

for threshold in range(max(l), 0, -1):
    for n in l:
        print("X" if n >= threshold else " ", end="")
    print()
