# Write your code here :-)
list = [8, 11, 24, 56, 88, 131]


def bsearch(list, ldx0, ldxn, val):
    if ldx0 > ldxn:
        return None
    else:
        midval = ldx0 + ((ldxn - ldx0) // 2)
    if list[midval] > val:
        return bsearch(list, ldx0, midval - 1, val)
    elif list[midval] < val:
        return bsearch(list, midval + 1, ldxn, val)
    else:
        return midval


print(bsearch(list, 0, 5, 24))
print(bsearch(list, 0, 5, 51))
