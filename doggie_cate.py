import codecs

dog_map = {}
file = codecs.open("C:\\Users\Administrator\Desktop\label_name.txt", 'r', 'utf-8')
while True:
    lines = file.readlines(10000)
    if not lines:
        break
    for line in lines:
        lineArr = line.split(" ")
        dog_map[lineArr[1]] = lineArr[0]
