def unique_in_order(iterable):
    uni = []

    if type(iterable) == list:
        iterable = "".join(iterable)

    for i in iterable :
        if i not in uni  or i != uni[-1]:
            uni.append(i)

    return uni