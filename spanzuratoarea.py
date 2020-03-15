from random import randint
from time import sleep


def eliminateDuplicates():
    with open("words.txt", "r") as file:
        s = set()
        for line in file:
            s.add(line)
    with open("words2.txt", "w") as file:
        for el in s:
            file.write(el)


def randomWordPick():
    with open("words2.txt", "r") as file:
        done = 0
        chance = 0
        print("0%")
        for line in file:
            done += 5
            if (done < 100):
                print(str(done) + "%")
                sleep(0.1)
            chance += 1
            if line != "" and randint(1, chance) == chance:
                picked = (line.split("\n"))[0]
        print("100%")
    return picked


def initHidden(word):
    hidden = ""
    for i in range(len(word)):
        if word[i] == " ":
            hidden += " "
        else:
            hidden += "-"
    return hidden


def play():
    print("\nO secunda sa aleg un cuvant.\n")
    word = randomWordPick().lower()
    hidden = initHidden(word)
    wrongLetters = []
    tries = 8  # standard

    print("START!\n")
    # print("Aveti", tries, "incercari")
    while tries != 0:
        print(hidden, " " * 10, "Greseli permise:", tries, " " * 10,"Litere gresite:",wrongLetters)
        gameInput = input("Dati o litera sau solutia: ").lower()
        if len(gameInput) != 1:
            if gameInput == word:
                break
            print("Solutia nu este buna -_-")
            continue
        check = checkHidden(word, hidden, gameInput, wrongLetters)
        if check is None:
            print("Ai ales deja aceasta litera o_O")
            continue
        elif check == True:
            newHidden = ""
            for i in range(len(word)):
                if word[i] == gameInput:
                    newHidden += gameInput
                else:
                    newHidden += hidden[i]
            hidden = newHidden
            if hidden == word:
                break
        else:
            tries -= 1
            wrongLetters.append(gameInput)
    if tries:
        print(word)
        print("Felicitari, ai castigat ^_^")
    else:
        print("Imi pare rau, ai pierdut -_-")
        print("Cuvantul era:", word)


def checkHidden(word, hidden, letter, wrongLetters):
    if (letter in hidden) or (letter in wrongLetters):
        return None
    elif letter in word:
        return True
    return False


if __name__ == '__main__':
    print("Bună!")
    answer = input("Vrei să te joci spânzurătoarea? (da/nu)\n").lower()
    if answer == "nu":
        print("Ok, pe data viitoare :)")
        exit()
    while answer == "da":
        play()
        answer = input("\nVrei să te joci din nou? (da/nu)\n").lower()
    else:
        print("Ok, pe data viitoare :)")
