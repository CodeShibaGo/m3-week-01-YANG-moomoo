def distinct(seq):
    dup = []
     
    for i in seq :
        if i not in dup:
            dup.append(i)

    return dup