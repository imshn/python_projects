import random as rn

words = ["python", "java", "javascript", "c", "golang", "erlang", "html", "css"]
word = rn.choice(words)

def replace_word_with_(string):
    dashed_word = [str(string).replace(i, "_") for i in string]
    return str(dashed_word).join("_")

def replaced_dashed_with(string, replaced):
    return string.replace(string[string.find(replaced)], replaced)
print("Guess the word! HINT: word is a name of a Computer Lang")
print(replace_word_with_(word))

while True:
    user_word = input("Enter a letter to guess: ")
    if user_word not in word:
        print("Opp! Wrong guess try again")
    else:
        replaced_dashed_with(word, user_word)
        break



