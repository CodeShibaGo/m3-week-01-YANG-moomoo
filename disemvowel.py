def disemvowel(s):
    vowels = "aeiouAEIOU"
    seq = ""

    for i in s:
        if i not in vowels:
            seq +=i

    return seq
