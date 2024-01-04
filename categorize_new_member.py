def categorize_new_member(data):

    for i in data :
        if not isinstance(i, tuple)  or  len(i) != 2 :
            return "Error: Input should be a list with two number"
    
    cate = []

    for age, score in data:
        if age >= 55 and score > 7:
            cate.append("Senior")
        else:
            cate.append("Open")

    return cate