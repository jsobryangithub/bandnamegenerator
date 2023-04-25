import random
import nltk


#opens the corpus of text which will be used
def readfile(name):
    with open (name) as f:
        contents = f.read()
        return contents

def bandname(textsource):
    number = random.randint(1,400)
    source = readfile(textsource)
    #Tokenizes the text into parts of speech
    tokens = nltk.word_tokenize(source)
    pos_tags = nltk.pos_tag(tokens)
    adjectives = [word for word, pos in pos_tags if pos.startswith("JJ")]
    nouns = [word for word, pos in pos_tags if pos.startswith("NN")]
    proper_nouns = [word for word, pos in pos_tags if pos.startswith("NNP")]
    plural_nouns = [word for word, pos in pos_tags if pos.startswith("NNS")]
    #adds random chance of producing various band name formats
    if number % 2 == 0:
        x = f"The {random.choice(adjectives).capitalize()} {random.choice(nouns).capitalize()}"
    elif number % 3 == 0:
        x = f"{random.choice(proper_nouns)} And The {random.choice(plural_nouns).capitalize()}"
    else:
        x = f"{random.choice(adjectives).capitalize()} {random.choice(nouns).capitalize()}"
    return x

def printnames():
    x = int(input('How many band names: '))
    for i in range(x):
        print(bandname('#TEXT FILE NAME GOES HERE'))

if __name__ == "__main__":
    printnames()
