def find_capitals(word):
    find = ""

    for i in range(len(word)):
        if word[i].islower() == False and word[i] != " ":
            find += word[i]

    return find.strip()
