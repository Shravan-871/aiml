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
                specific[x]='?'
                general[x][x]='?'
            elif i[-1]=='no':
                for j in range (len(specific[j])):
                    if i[j]!=specific[x]:
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
