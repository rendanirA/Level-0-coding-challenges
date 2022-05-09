def find_vowels(string1):
    results = ""
    for char in string1:
        if char in "aeiouAEIOU":
            results = results + char
    else:
        result = ",".join(sorted(set(results), key=results.index))
    return result


string1 = "Umuzi"
vowels = find_vowels(string1.lower())
print("vowels : " + vowels, sep=",")
