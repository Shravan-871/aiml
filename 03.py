'''For a given set of training data examples stored in a .CSV file, implement
and demonstrate the Candidate-Elimination algorithm to output a
description of the set of all hypotheses consistent with the training
examples.'''

import csv
with open ("03.csv") as f:
        csv_file=csv.reader(f)
        data = list(csv_file)
        specific=data[0][:-1]
        general=[['?']*len(specific)]*len(specific)
print(specific)
print("--------------")
        
for i in data:
    if i[-1] =="yes":
        for j in range (len(specific)):
            if i[j]!=specific[j]:
                specific[j]='?'
                general[j][j]='?'
            elif i[-1]=='no':
                for j in range (len(specific[j])):
                    if i[j]!=specific[j]:
                        general[j][j]=specific[j]
                    else:
                        general[j][j]='?'
    print("\nstep "+str(data.index(i)+1)+" of candidate elimination algorithm\n")
    print(specific,"\n")
    print(general,"\n")

print("--------------")

gh=[]
for i in general:
    print(i)
    for j in i:
        print(j)
        if j!="?":
            gh.append(i)
            break
print(specific)
print(gh)
