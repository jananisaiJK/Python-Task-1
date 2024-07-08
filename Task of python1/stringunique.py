def check_unique(string):
    unique_characters = []
    for character in string:
        if character in unique_characters:
            return False
        else:
            unique_characters.append(character)
    return True
test = "abcbd"

print(check_unique(test))