import fileinput
import sys

# Testing something


def getFile():
    inp = input("Enter the name of the file to use:")
    try:
        for line in fileinput.input(inp):
            bool_word = False
            array_words = []
            word = []
            for i in range(0, len(line)):
                if bool_word and line[i] != "]":
                    if line[i] == "-":
                        word.append(" ")
                    else:
                        word.append(line[i])
                if line[i] == "[":
                    del word[:]
                    bool_word = True
                elif line[i] == "]":
                    array_words.append(''.join(word))
                    bool_word = False
            words = getWords(array_words)
            print("Here is your story\n-------------------")
            print(replace(line, words))
    except OSError:
        print("Error Bad File Name")
        sys.exit(0)


def getWords(arr):
    words = []
    for i in range(len(arr)):
        if arr[i][0] == "a" or arr[i][0] == "e" or arr[i][0] == "i" or arr[i][0] == "o" or arr[i][0] == "u":
            print("Please give an {}".format(arr[i]))
        else:
            print("Please give a {}".format(arr[i]))
        inp = input()
        words.append(inp)
    return words


def replace(file, words):
    counter = 0
    file = file.split()
    for i in range(len(file)):
        if file[i][0] == "[":
            if file[i][-1] == "." or file[i][-1] == ",":
                file[i] = words[counter] + file[i][-1]
            else:
                file[i] = words[counter]
            counter += 1
    file = " ".join(file)
    return file


getFile()