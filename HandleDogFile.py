import codecs

def readData_train_img():
    file = open("C:\\Users\\Administrator\\Desktop\\data_train_image.txt")
    fileOut = open("C:\\Users\\Administrator\\Desktop\\data_train_image_tp.txt","w+")

    outlines=[]
    outlines.append("id,imgUrl\n")
    while True:
        lines = file.readlines(10000)
        if not lines:
            break
        for line in lines:
            lineArr = line.split(" ")
            out = lineArr[1]+","+lineArr[0]+"\n"
            outlines.append(out)
    fileOut.writelines(outlines)
    file.close()
    fileOut.close()

def readValCsv():
    file = open("C:\\Users\\Administrator\\Desktop\\val.txt")
    fileOut = open("C:\\Users\\Administrator\\Desktop\\val.csv","w+")

    outlines=[]
    outlines.append("id,imgUrl\n")
    while True:
        lines = file.readlines(10000)
        if not lines:
            break
        for line in lines:
            lineArr = line.split(" ")
            out = lineArr[1]+","+lineArr[2]
            outlines.append(out)
    fileOut.writelines(outlines)
    file.close()
    fileOut.close()

def readTrain():
    file = open("C:\\Users\Administrator\Desktop\data_train.txt")
    fileOut = open("C:\\Users\Administrator\Desktop\data_train.csv", "w+")

    outlines = []
    outlines.append("id,imgUrl\n")
    while True:
        lines = file.readlines(10000)
        if not lines:
            break
        for line in lines:
            lineArr = line.split(" ")
            out = lineArr[0] + "," + lineArr[1]
            outlines.append(out)
    fileOut.writelines(outlines)
    file.close()
    fileOut.close()

def readLabel():
    file = codecs.open("C:\\Users\Administrator\Desktop\label_name.txt",'r', 'utf-8')
    fileOut = codecs.open("C:\\Users\Administrator\Desktop\label_name.csv", 'w+', 'utf-8')

    outlines = []
    outlines.append("name,id\n")
    while True:
        lines = file.readlines(10000)
        if not lines:
            break
        for line in lines:
            lineArr = line.split(" ")
            out = lineArr[0] + "," + lineArr[1]
            outlines.append(out)
    fileOut.writelines(outlines)
    file.close()
    fileOut.close()

readData_train_img()
# readValCsv()
# readTrain()
# readLabel()