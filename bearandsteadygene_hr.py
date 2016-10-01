def everythingMatch(dictToFind,dictOfWord):
    for key, _value in dictToFind.items():
        if (key in dictOfWord):
            if dictToFind[key]>dictOfWord[key]:
                return False
        else:
            return False
    return True       
def findsubString(dictToFind,word): 
    index1=0
    index2=0
    myDict={}
    matched=0
    previousMatch=0
    while index2<len(word):
        if everythingMatch(dictToFind,myDict):
            previousMatch=matched
            matched=index2-index1
            if previousMatch!=0:
                matched=min(previousMatch,matched)                
            myDict[word[index1]]-=1
            index1+=1
        else:
            if word[index2] in myDict:
                myDict[word[index2]]+=1
            else:
                myDict[word[index2]]=1
            index2+=1;
    return matched

            
            
lenOfString=int(input())
letterDict = {'G': 0, 'C': 0, 'T': 0,'A':0}
dictToFind=dict()
word=input()
for eachLetter in word:
    letterDict[eachLetter]+=1
for key, value in letterDict.items():
    if value>(lenOfString/4):
        dictToFind[key]=value-lenOfString/4
if (any(dictToFind)):
    print (findsubString(dictToFind,word))
else:
    print (0)