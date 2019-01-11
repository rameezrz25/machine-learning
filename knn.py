import csv
import random
import operator
import math
with open('IRIS.csv','r') as csvfile:
    lines=csv.reader(csvfile)
    next(lines)
    dataset=list(lines)
    #print(len(dataset))
folds=[]
def shuffle(i_data):
    random.shuffle(i_data)
    #print(i_data)
    length = int(len(i_data) / 10)  # length of each fold
    #print(length)
    folds=[]
    for i in range(10):
        folds += [i_data[i * length:(i + 1) * length]]
    folds += [i_data[9 * length:len(i_data)]]
    #print(folds)
    return(folds)
    #train_data = i_data[:int(0.9*100)]
    #test_data = i_data[int(0.9*100):]
    #return train_data, test_data


def euclideanDist(x, xi):
    d = 0.0
    for i in range(len(x) - 1):
        #print(x[i], xi[i])
        d += pow((float(x[i]) - float(xi[i])), 2)  # euclidean distance

    d = math.sqrt(d)
    #print(d)
    return d


# KNN prediction and model training
def knn_predict(test_data, train_data, k_value):
    for i in test_data:
        eudistance = []
        knn = []
        irisversicolor=0
        irissetosa=0

        for j in train_data:
            eu_dist = euclideanDist(i, j)
            eudistance.append([j[4], eu_dist])
            eudistance.sort(key=operator.itemgetter(1))
            knn = eudistance[:k_value]
            for k in knn:
                if k[0] == 'Iris-versicolor':
                    irisversicolor += 1
                else:
                    irissetosa += 1
        if irisversicolor > irissetosa:
            i.append('Iris-versicolor')
        elif irisversicolor < irissetosa:
            i.append('Iris-setosa')
        else:
            i.append('NaN')

    return  eudistance


def accuracy(test_data):
    correct = 0
    for i in test_data:
        if i[4] == i[5]:
            correct += 1
    accuracy = float(correct)/len(test_data) *100  #accuracy
    return accuracy

folds=shuffle(dataset)
for l in range(10):
    print('k fold',l+1)
    for j in range(3, 12, 1):
        acc = 0
        print('for k =', j)
        for i in range(10):
            knn_predict(folds[l], folds[i], j)
            #print(accuracy(folds[l]))
            acc += accuracy(folds[l])
            for k in range(0, 10, 1):
                del folds[l][k][5]
        print('accuracy', acc/10)
