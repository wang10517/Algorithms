def replaceSpace(string, trueLen):
    string = list(string)
    spaceCounter = 0
    index = 0
    for i in range(trueLen):
        if string[i] == ' ':
            spaceCounter += 1

    index = trueLen + spaceCounter*2
    if index > len(string):
        return -1

    for i in range(trueLen-1, -1, -1):
        char = string[i]
        if char == ' ':
            string[index-3: index] = ['%', '2', '0']
            index -= 3
        else:
            string[index-1] = char
            index -= 1
    return ''.join(string[0:trueLen + spaceCounter*2])
