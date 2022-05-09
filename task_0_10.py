def find_common_characters(string1, string2):
    results = ""
    for char in string1:
        if char in string2:
            results = results + char
    else:
        result = ",".join(sorted(set(results), key=results.index))
    return result


string1 = "House"
string2 = "Computers"
common_characters = find_common_characters(string1.lower(), string2.lower())
print("common letters: " + common_characters, sep=",")
