def sum_of_squares(lista):
    return (lambda x: sum(l**2 for l in x))(lista)

assert(sum_of_squares([2, 3, 4]) == 29)
assert(sum_of_squares([ ]) == 0)
assert(sum_of_squares([2, -3, 4]) == 29)