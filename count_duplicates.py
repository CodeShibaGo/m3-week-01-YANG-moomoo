def count_duplicates(text):
    text = text.lower()
    dup = []
    count = 0

    for i in text:
        if text.count(i) > 1 and i not in dup:
            count += 1
            dup.append(i)


    return count