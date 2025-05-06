import sys
from stats import getNoOfWords, getNoOfCharacters, sortCharDict


def main():
    try:
        contentsOfFile = getBookText(sys.argv[1])
        noOfWords = getNoOfWords(contentsOfFile)
        numberOfWords = len(noOfWords)

        charDict = getNoOfCharacters(contentsOfFile)
        sortedCharDict = sortCharDict(charDict)
        print(f"Found {numberOfWords} total words")
        for k in sortedCharDict:
            if k["char"].isalpha():
                print(f"{k["char"]}: {k["num"]}")
    except Exception as e:
        print(f"Error encountered: {e}")
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    

def getBookText(filepath):
    with open(filepath) as f:
        contentsOfFile = f.read()
        return contentsOfFile 

main()