def count_up_to_sam(list):
    counter = 0
    for l in list:
        counter += 1
        if l == "sam":
            break
        
    return counter

assert(count_up_to_sam(["a", "b", "c"]) == 3)
assert(count_up_to_sam(["a", "sam", "c"]) == 2)
assert(count_up_to_sam(["sam", "b", "sam"]) == 1)
assert(count_up_to_sam(["sam", "sam", "c"]) == 1)