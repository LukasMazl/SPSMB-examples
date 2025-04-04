#udělej 2 metody. 
#1)první bude do slovníku zapisovat jako klíč(key) slovo a jako hodnotu(value) ASCII hodnotu klíče.
#2)druhá bude na základě ASCII kódu, které je ve slovníku, vracet slovo ze slovníku.

word_and_hash = {}

def addword(word):
    word_to_list = list(word)
    final_word = ""
    for element in word_to_list:
        final_word += f"{ord(element)}"

    word_and_hash[word] = final_word

def get_word_from_hash(word_hash):
    final_word = ""
    for value, key in word_and_hash.items():
        if key == word_hash:
            final_word = value
    return final_word

addword("jablko")

word_hash = None

for key, value in word_and_hash.items():
    if key == "jablko":
        word_hash = value
        break

print(f"{word_hash}: {get_word_from_hash(word_hash)}")