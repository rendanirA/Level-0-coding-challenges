def find_common_characters(string1, string2):
    res = " "
    for char in string1:
        if char in string2:
            res = res + char
    else:
        x = " ".join(sorted(set(res), key=res.index))
    return x


string1 = "house"
string2 = "computers"
common_characters = find_common_characters(string1, string2)
print("common letters: ", common_characters, end=",")
