import json
import collections.abc
import pdb


CONFIG_FILE = "configurationFile.json"
CHANGES_FILE = "changes.txt"


'''
FUNCTION DEFINITION : Function that modifies values in the configuration file
on position specified by (.txt) file containing changes.
First parameter: configuration file
Second parameter: txt file containing list of changes to be applied
The resulting json is written into json file called resultConfiguration_v3.json
'''
def updateJsonFile(configFile, changesFile):

    changesDict = changesParser(changesFile)

    with open(configFile, "r") as readConfigFile:
        configData = json.load(readConfigFile)

    updateDictIteration(configData,changesDict)
        

    with open("resultConfiguration_v3.json", "w") as outfile:
        json.dump(configData, outfile, indent="   ")

    return 1



# Function allowing to put changes of txt file into a dictionary

def changesParser(changesFile):
    with open(changesFile, "r") as readChangesFile:
        content = readChangesFile.readlines()

    content = [x.strip() for x in content]
    
    finalDict = {}
    for line in content:
        tempDictionary = current = {}
        left, right = line.split(": ",1)
        leftList = left.replace("\"", "").split(".")
        for element in leftList[:-1]:
            current[element] = {}
            current = current[element]

        current[leftList[-1]] = json.loads(right)
        current = current[leftList[-1]]
        
        updateDictIteration(finalDict, tempDictionary)

    return finalDict



def updateDictIteration(oldDict, changes):
    pdb.set_trace()
    stack = [(oldDict,changes)]
    
    while stack:
      oldDict,changes = stack.pop()
      for x,y in changes.items():
         if isinstance(y, collections.abc.Mapping):
            tempDict = oldDict.setdefault(x, {})

            if isinstance(tempDict, collections.abc.Mapping):
               stack.append((tempDict, y))
               
            else:
               oldDict[x] = y
            
         else:
            oldDict[x] = y


def updateDictRecursion(oldDict, changes):
    for x, y in changes.items():
        if isinstance(y, collections.abc.Mapping):
            oldDict[x] = updateDictRecursion(oldDict.get(x, {}), y)
        else:
            oldDict[x] = y
     
    return oldDict




    


def main():
    updateJsonFile(CONFIG_FILE, CHANGES_FILE)

if __name__ == "__main__":
    main()

