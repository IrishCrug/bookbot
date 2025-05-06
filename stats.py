def getNoOfWords(fileContents):
    return fileContents.split()

def getNoOfCharacters(fileContents):
    characterDict = {}
    charList = []
    lowerCaseContents = fileContents.lower()
    charList = list(lowerCaseContents) 
    for l in charList:
        if characterDict:
            if l in characterDict:
                characterDict[l] += 1
            elif l not in characterDict:
                characterDict[l] = 1
        else:
            characterDict[l] = 1 
    return characterDict

def sortCharDict(characterDict):
    dictAddedToList =[]
    for k in characterDict:
        sortedCharDict = {}
        sortedCharDict["char"] = k
        sortedCharDict["num"] = characterDict[k]
        dictAddedToList.append(sortedCharDict)
    dictAddedToList.sort(reverse=True, key=sortOn)
    
    return dictAddedToList 
    


def sortOn(dict):
    return dict["num"]