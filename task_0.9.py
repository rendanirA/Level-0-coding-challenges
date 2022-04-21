def find_vowels(string1):
    res = ""
    for char in string1:
        if char in "aeiouAEIOU":
            res = res + char
    else:
        x = ",".join(sorted(set(res), key=res.index))
    return x


string1 = "Umuzi"
vowels = find_vowels(string1.lower())
print("vowels : " + vowels, sep=",")
