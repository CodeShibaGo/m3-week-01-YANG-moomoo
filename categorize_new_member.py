def categorize_new_member(data):

    for i in data :
        if not all(isinstance(i, list) and len(i) == 2 ):
            return "Error: Input should be a list with two integers each"
    
    cate = []

    for age, score in data:
        if age >= 55 and score > 7:
            cate.append("Senior")
        else:
            cate.append("Open")

    return cate