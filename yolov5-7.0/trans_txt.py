import os
import random
trainval_percent = 0.2
train_percent = 0.8
xmlfilepath = 'data/images'
txtsavepath = 'data/ImageSets'
total_xml = os.listdir(xmlfilepath)
num = len(total_xml)
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)
ftrainval = open('data/ImageSets/trainval.txt', 'w')
ftest = open('data/ImageSets/test.txt', 'w')
ftrain = open('data/ImageSets/train.txt', 'w')
fval = open('data/ImageSets/val.txt', 'w')
for i in list:
    name = total_xml[i][:] + '\n'
    if i in trainval:
        ftrainval.write('data/images/' + name)
        if i in train:
            ftest.write('data/images/' + name)
        else:
            fval.write('data/images/' + name)
    else:
        ftrain.write('data/images/' + name)
ftrainval.close()
ftrain.close()
fval.close()
ftest.close()

