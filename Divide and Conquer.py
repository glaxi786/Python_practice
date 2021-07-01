# divide and conquer algorithms with python
list = [2, 7, 19, 34, 53, 72]


def bsearch(list, val):
    list_size = len(list) - 1

    ldx0 = 0
    ldxn = list_size

    while ldx0 <= ldxn:
        midval = (ldx0 + list_size) // 2

        if list[midval] == val:
            return midval
        if val > list[midval]:
            ldx0 = midval + 1
        else:
            ldxn = midval - 1
    if ldx0 > ldxn:
        return None


print(bsearch(list, 19))
print(bsearch(list, 11))
