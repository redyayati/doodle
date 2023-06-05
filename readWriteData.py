import numpy as np 

def makeBin(filename , num) : 
    path = f'ML/doodle/data/npy/{filename}.npy'
    data = np.load(path)
    allDraw = data[0]
    if num > 1 : 
        for i in range(num-1) : 
            draw = data[i+1]
            allDraw = np.concatenate((allDraw , draw))
    byteallDraw = bytearray(allDraw)
    outputFile = f'{filename}{num}'
    writeData(byteallDraw ,outputFile)
def writeData(array , filename) :
    path =  f'ML/doodle/data/bin/{filename}.bin'
    array = bytearray(array)
    with open(path,'wb') as f :
        f.write(array)
        f.close()
def readData(filename) : 
    path = f'ML/doodle/data/bin/{filename}.bin'
    with open(path,'rb') as f :
        data = f.read()
        f.close
    data = toDec(data)
    return data  
def toDec(array) : 
    data = []
    for i in range(len(array)) : 
        data.append(int(array[i]))
    return data

# # makeBin('airplane' , 2)

# print(len(readData('airplane2')))
