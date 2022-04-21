def find_common_characters(string1, string2):
    res = ""
    for char in string1:
        if char in string2:
            res = res + char
    else:
        x = ",".join(sorted(set(res), key=res.index))
    return x


string1 = "House"
string2 = "Computers"
common_characters = find_common_characters(string1.lower(), string2.lower())
print("common letters: " + common_characters, sep=",")
