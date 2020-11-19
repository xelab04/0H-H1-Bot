text = ""
array = []
matrix = []

while text != "@":
    text = input(">>> ")
    if text != "@":
        array.append(text)

for line in array:
    text = ""
    for i in range(len(array)):
        if i > 0:
            text = text + "," + line[i]
        else:
            text = line[i]
    print(text)
