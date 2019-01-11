import csv
import random
import operator
import math
file=input(('enter the filename'))
with open(file,'r') as csvfile:
    lines=csv.reader(csvfile)
    next(lines)
    data=list(lines)
    #random.shuffle(data)

k1 = []
k2 = []
labels = []
totalYes=0
totalno=0
for i in data:
    if i[0]=='Yes':
        totalYes+=1
    else:
        totalno+=1
print(totalYes,totalno)

k1.append(data[0])
k2.append(data[1])

mean1 = k1[0][0:]
mean2 = k2[0][0:]


def findmean(cluster):
    n = len(cluster)
    mean = [0] * len(cluster[0])
    for i in range(1, len(cluster[0])):
        for j in range(len(cluster)):
            mean[i] += float(cluster[j][i])
    return [float(g / n) for g in mean]


while (1):
    for i in data:
        d1 = 0
        d2 = 0
        for j in range(1, len(i)):
            d1 += (float(mean1[j]) - float(i[j]))* (float(mean1[j]) - float(i[j]))
            d2 += (float(mean2[j]) - float(i[j]))*(float(mean2[j]) - float(i[j]))
        d1 = math.sqrt(d1)
        d2 = math.sqrt(d2)

        if d1 < d2:
            k1.append(i)
        else:
            k2.append(i)

    newmean1 = findmean(k1)
    newmean2 = findmean(k2)

    if newmean1 == mean1 and newmean2 == mean2:
        break
    else:
        mean1 = newmean1[:]
        mean2 = newmean2[:]
    k1, k2 = [], []

k1_labels, k2_labels = [], []
k1Yes = 0
k1No = 0
k2No = 0
k2Yes = 0

for i in k1:
    if(i[0] =='Yes'):
        k1Yes+=1
    else:
        k1No+=1

for i in k2:
    if (i[0] == 'Yes'):
        k2Yes += 1
    else:
        k2No += 1

if k1Yes > k1No:
    print("Accuracy Cluster 1:", float(k1Yes / totalYes))
else:
    print("Accuracy Cluster 1:", float(k2No / totalno))

if k2Yes > k2No:
    print("Accuracy Cluster 2:", float(k2Yes / totalYes))
else:
    print("Accuracy Cluster 2:", float(k2No / totalno))
