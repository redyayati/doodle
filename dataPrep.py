import readWriteData as rw
from nn import NeuralNetwork
import random
import pickle
# # Make binary file 
# rw.makeBin('airplane' , 1000)
# rw.makeBin('apple' , 1000)
# rw.makeBin('cat' , 1000)
# rw.makeBin('rainbow' , 1000)
# read binary files 
# a = rw.readData('cat1000') 

cats_data = rw.readData('cat1000')
airplane_data = rw.readData('airplane1000')
rainbow_data = rw.readData('rainbow1000')
# apple_data = rw.readData('apple1000')

# print(len(cats))
# print(len(rainbow))
# print(len(airplane))

cats = {'training':[] , 'testing':[]}
airplane = {'training':[] , 'testing':[]}
rainbow = {'training':[] , 'testing':[]}
apple = {'training':[] , 'testing':[]}

length = 784
def prepareData(catagory , data , label) : 
    for i in range(1000) : 
        array = []
        for j in range(length) : 
            index = i*length  + j 
            array.append(data[index])
        if i < 800 :
            array.append(label)  # last element is the label 
            catagory['training'].append(array)
        else : 
            array.append(label)  # last element is the label
            catagory['testing'].append(array)
            

cat_label = 0
airplane_label = 1
rainbow_label = 2
apple_label = 3

prepareData(cats , cats_data , cat_label)
prepareData(airplane , airplane_data , airplane_label)
prepareData(rainbow , rainbow_data , rainbow_label)
# prepareData(apple , apple_data , apple_label)

# print(len(cats['training']) , len(cats['testing']))
# print(len(airplane['training']), len(airplane['testing']))
# print(len(rainbow['training']), len(rainbow['testing']))
# print(len(apple['training']), len(apple['testing']))

# print(cats['testing'][100])

nn = NeuralNetwork(784 , 64 ,3)

training = [] 
training.extend(cats['training'])
training.extend(airplane['training'])
training.extend(rainbow['training'])
# training.extend(apple['training'])




# Traing : 
def trainEpoch(data) : 
    print(f'Starting to train with {len(data)} datas...')
    random.shuffle(data)
    n = len(data)
    for i in range(1) :
        inputs = []
        dataArray = data[400][:784]
        for j in range(len(dataArray)) : 
            element = dataArray[j] / 255
            inputs.append(element)
        label = data[i][784]
        targets = [0,0,0]
        targets[label] = 1 
        nn.train(inputs , targets)
    print("trained for one epoch")


# with open('ML/doodle/data/nn.obj' , 'wb') as f :  # For saving the model
#         pickle.dump(nn , f)

# print(inputs)
# print(len(inputs))
# print(label)
# print(targets)

# trainEpoch(training)


testing = []
testing.extend(cats['testing'])
testing.extend(airplane['testing'])
testing.extend(rainbow['testing'])
# print(len(testing))
# print(len(testing[1]))
# print(testing[550][784])

xtras = {'training':[] , 'testing':[]}
new = []
for i in range(200) : 
    array = []
    for j in range(length) : 
        index = (i+200)*length  + j 
        array.append(airplane_data[index])
    array.append(1)  # last element is the label 
    xtras['testing'].append(array)

# print(len(xtras['testing']))
# print(xtras['testing'][1])
testing.extend(xtras['testing'])

# Testing : 
with open('ML/doodle/data/nn.obj' , 'rb') as f : 
        model = pickle.load(f)

def testAll(testing) : 
    correct = 0
    n = len(testing)
    t = 50
    for i in range(n) :
        inputs = []
        testingArray = testing[i][:784]
        for j in range(len(testingArray)) : 
            element = testingArray[j] / 255
            inputs.append(element)
        label = testing[i][784]
        guess = model.predict(inputs)
        guessIndex = guess.index(max(guess))
        if label == guessIndex : correct += 1 
    print("done testing ! ")
    print("percentage correct : " + str(correct * 100/n))
    
# Single data test :
def singleTest(testData) : 
    inputs = []
    testingArray = testData[:784]
    for j in range(len(testingArray)) : 
        element = testingArray[j] / 255
        inputs.append(element)
    label = testData[784]
    guess = model.predict(inputs)
    guessIndex = guess.index(max(guess))
    print("done testing ! ")
    print(guess)
    print("label is : ", label)
    print("predicted : " , guessIndex)

# singleTest(testing[10])

testAll(testing)
