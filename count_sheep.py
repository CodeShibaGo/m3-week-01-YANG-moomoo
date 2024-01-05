def count_sheep(sheep):

    for i in sheep :
        if not isinstance(i, bool):
            return "Error: List not boolean values"

    return(sheep.count(True))
