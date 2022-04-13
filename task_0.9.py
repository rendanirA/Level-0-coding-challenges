def prints_out_vowels_in_string(string):
    string1 = set(string)
    for char in string1:
        if char in "aeiouAEIOU":
            print(char, end=",")
    return char


string1 = "umuzi"
prints_out_vowels_in_string(string1)
