def categorize_new_member(data):
    
    cate = []

    for age, score in data:
        if age >= 55 and score > 7:
            cate.append("Senior")
        else:
            cate.append("Open")

    return cate