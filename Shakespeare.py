## Starting from Shakespeare example in class notes

from VSG_Module import *

D = {}

F = open("Shakespeare.txt", mode = "rU")
s = F.read()
F.close()

Words = s.split()   # Makes a list of all the whitespace-separated words in
                    #   the doc

counter = 0
limit = len(Words)-5

for w in Words:
    if counter < limit:
        if Words[counter] == Words[counter].upper():
            if Words[counter+4][-1] == "!":
                fiveMer = " ".join(Words[counter:counter+5])
                if not (fiveMer in D):
                    D[fiveMer] = 0
                D[fiveMer] += 1
        else:
            D[w] = 1    # New word - start its counter at 1
    else:
        break
    counter += 1

for fiveMerKey in D:
    if D[fiveMerKey] > 1:
        print(fiveMerKey + "\t" + (str(D[fiveMerKey]))
