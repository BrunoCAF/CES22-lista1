def sum_but_not_first_even(list):
    drop = False
    S = 0
    for l in list:
        if (l % 2 == 0) and not drop:
            drop = True
            continue
        S += l

    return S

assert(sum_but_not_first_even([3,3,1,3]) == 10)
assert(sum_but_not_first_even([3,3,1,3,2,2,2,5,7,6]) == 32)
assert(sum_but_not_first_even([0,1,0,1,2,0]) == 4)
assert(sum_but_not_first_even([1,2,3,4,5,6,7,8,9,0]) == 43)
