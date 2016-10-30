wordsTable = []

def buildDictionary():
    with open("supportFiles/dictionary.txt") as f:
        global wordsTable
        wordsTable = f.read().splitlines()
        print wordsTable

def isWord(word):
    print "nope"

buildDictionary()
print wordsTable

