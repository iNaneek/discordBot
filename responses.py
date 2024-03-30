import random
from copy import deepcopy

#/removetimeout user:@Rubics Bot#3734 reason:bc



printableMat = [ #defines the matrix, printed out instead of automated for testing
        [0, 0, 0, 0], #for simplicity, these are presented to player are 2^x
        [0, 0, 0, 0], #so a 128 on the board is a 7 and 2048 is an 11
        [0, 0, 0, 0], #this makes logic simpler to handle
        [0, 0, 0, 0]
    ]



#refrenceMat = 0 #redefined later, but refrenced in functions


running = True #when set as false, the window closes. used in whileloop further down

def getGameStatus(mat): #determines if game is over or not, not yet implemented
    for y in range(4):
        for x in range(4):
            if mat[y][x] == 0: #if any 0 is found then the game is still in progress
                return 1


def twoOrFour(): #this returns a 2 or a 4, because when a move is made, a four has a 20% chance to appear
    number = random.randint(1, 5)
    if number == 1:
        return 2 #prints 4
    else:
        return 1 #prints 2

def newNumberOnMat(mat): #imput a matrix, and replace a random 0 with a 1 or a 2, uses previous funtion
    print('new')
    print(printableMat)
    while True:
        rand1 = random.randint(0, 3)
        rand2 = random.randint(0, 3)
        if mat[rand1][rand2] == 0:
            mat[rand1][rand2] = twoOrFour()
            break
    return mat

printableMat = newNumberOnMat(newNumberOnMat(printableMat))

def transpose4x4Mat(matTranspose):
    matTranspose2 = []
    for i in range(4):
        matTranspose2.append([])
        for j in range(4):
            matTranspose2[i].append(matTranspose[j][i])
    return matTranspose2

def shift(shiftRow):
    #this function takes a 4 integer row and takes out all 0s and then adds the 0s again
    #for example: input[0,2,0,2] and get an output of [2,2,0,0]
    #this is neccissary for the next function
    shiftRowReturn = [] #makes a second list used to add elements in the new order
    blanks = 0 #acts as a counter and re adds this many 0s
    for i in range(4):
        if shiftRow[i] == 0: blanks = blanks + 1
        else: shiftRowReturn.append(shiftRow[i])
    for i in range(blanks):shiftRowReturn.append(0)
    return shiftRowReturn

def compile(compileRowInput):
    compileRow = compileRowInput.copy()
    #for example input=[1,2,0,2] and then output=[1,3,0,0] (for pushing left only)
    for i in range(3): #3 is the perfect number bc it combines numbers for [1,1,0,0] [0,1,1,0] and [0,0,1,1]
        compileRow = shift(compileRow)
        if (compileRow[i] != 0) and (compileRow[i] == compileRow[i + 1]):
            compileRow[i + 1] = 0
            compileRow[i] = compileRow[i] + 1
    return compileRow





def compileMat(compileFuncMat):
    for i in range(4):
        compileFuncMat[i] = compile(compileFuncMat[i])
    return compileFuncMat


def left(leftMatTemp):
    leftMatTemp = compileMat(leftMatTemp)
    return leftMatTemp


def right(rightMatTemp):
    for i in range(4):
        rightMatTemp[i].reverse()
        rightMatTemp[i] = compile(rightMatTemp[i])
        rightMatTemp[i].reverse()
    return rightMatTemp

def up(upMatTemp):
    upMatTemp = transpose4x4Mat(upMatTemp)
    upMatTemp = left(upMatTemp)
    upMatTemp = transpose4x4Mat(upMatTemp)
    return upMatTemp

def down(downMatTemp):
    downMatTemp = transpose4x4Mat(downMatTemp)
    downMatTemp = right(downMatTemp)
    downMatTemp = transpose4x4Mat(downMatTemp)
    return downMatTemp



def compareMatrixes(mat1, mat2):
    for i in range(4):
        for j in range(4):
            if mat1[i][j] != mat2[i][j]:
                return True
    print('MOVE NOT POSSIBLE')
    return False

conversions = {0: ':black_small_square:',
               1: ' 2 ',
               2: ' 4 ',
               3: ' 8 ',
               4: ' 16 ',
               5: ' 32 ',
               6: ' 64 ',
               7: '128',
               8: '256',
               9: '512',
               10: '888',
               11: '999'}

def format_2d_array(mat):
    mat2 = deepcopy(mat)
    for row in range(4):
        for item in range(4):
            mat2[row][item] = conversions[mat2[row][item]]
    print(mat2)
    formatted = ""
    for row in mat2:
        formatted += ':black_small_square:'
        formatted += "".join(map(str, row)) + "\n"  # Join each element in the row with a space

    return formatted

import csv

def read_csv_file(filename):
    data = []
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data

def write_csv_file(filename, data):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for row in data:
            writer.writerow(row)

# Example usage
filename = 'data.csv'
csv_data = read_csv_file(filename)
print(csv_data)






def handle_response(message, emojis):
    global printableMat
    p_message = message.content.lower()

    print(p_message)
    print(message.channel.id)
    csv_data.append((message.author.name, p_message.replace('\n', '-return-').replace(',', ''), "end message"))

    if str(message.channel.id) != "1116199621144883260" and str(message.guild.id) == "1084913611828383744":
        return None

    #f"{emojis[printableMat[0][0]]}{emojis[printableMat[0][1]]}{emojis[printableMat[0][2]]}{emojis[printableMat[0][3]]} \n{emojis[printableMat[1][0]]}{emojis[printableMat[1][1]]}{emojis[printableMat[1][2]]}{emojis[printableMat[1][3]]} \n{emojis[printableMat[2][0]]}{emojis[printableMat[2][1]]}{emojis[printableMat[2][2]]}{emojis[printableMat[2][3]]} \n{emojis[printableMat[3][0]]}{emojis[printableMat[3][1]]}{emojis[printableMat[3][2]]}{emojis[printableMat[3][3]]}"



    if p_message == 'test':

        u = f"hehehe {emojis[0]} {emojis[1]}" + "\n"
        return u

    if p_message == 'roll':
        return (str(random.randint(1,6)))

    if p_message == '!help':
        return "`do the helpy thing`"

    if p_message == 'save':
        write_csv_file("data.csv", csv_data)
        return "done"


    if p_message == 'print':
        print(printableMat)
        return f"{emojis[printableMat[0][0]]}{emojis[printableMat[0][1]]}{emojis[printableMat[0][2]]}{emojis[printableMat[0][3]]} \n{emojis[printableMat[1][0]]}{emojis[printableMat[1][1]]}{emojis[printableMat[1][2]]}{emojis[printableMat[1][3]]} \n{emojis[printableMat[2][0]]}{emojis[printableMat[2][1]]}{emojis[printableMat[2][2]]}{emojis[printableMat[2][3]]} \n{emojis[printableMat[3][0]]}{emojis[printableMat[3][1]]}{emojis[printableMat[3][2]]}{emojis[printableMat[3][3]]}"

    if p_message == 'a':
        if compareMatrixes(printableMat, left(deepcopy(printableMat))):
            printableMat = left(printableMat)
            printableMat = newNumberOnMat(printableMat)
            return f"{emojis[printableMat[0][0]]}{emojis[printableMat[0][1]]}{emojis[printableMat[0][2]]}{emojis[printableMat[0][3]]} \n{emojis[printableMat[1][0]]}{emojis[printableMat[1][1]]}{emojis[printableMat[1][2]]}{emojis[printableMat[1][3]]} \n{emojis[printableMat[2][0]]}{emojis[printableMat[2][1]]}{emojis[printableMat[2][2]]}{emojis[printableMat[2][3]]} \n{emojis[printableMat[3][0]]}{emojis[printableMat[3][1]]}{emojis[printableMat[3][2]]}{emojis[printableMat[3][3]]}"
        else:
            return f"fuck you {message.author.name}, you cant do that"
    if p_message == 'w':
        if compareMatrixes(printableMat, up(deepcopy(printableMat))):
            printableMat = up(printableMat)
            printableMat = newNumberOnMat(printableMat)
            return f"{emojis[printableMat[0][0]]}{emojis[printableMat[0][1]]}{emojis[printableMat[0][2]]}{emojis[printableMat[0][3]]} \n{emojis[printableMat[1][0]]}{emojis[printableMat[1][1]]}{emojis[printableMat[1][2]]}{emojis[printableMat[1][3]]} \n{emojis[printableMat[2][0]]}{emojis[printableMat[2][1]]}{emojis[printableMat[2][2]]}{emojis[printableMat[2][3]]} \n{emojis[printableMat[3][0]]}{emojis[printableMat[3][1]]}{emojis[printableMat[3][2]]}{emojis[printableMat[3][3]]}"
        else:
            return f"fuck you {message.author.name}, you cant do that"
    if p_message == 's':
        if compareMatrixes(printableMat, down(deepcopy(printableMat))):
            printableMat = down(printableMat)
            printableMat = newNumberOnMat(printableMat)
            return f"{emojis[printableMat[0][0]]}{emojis[printableMat[0][1]]}{emojis[printableMat[0][2]]}{emojis[printableMat[0][3]]} \n{emojis[printableMat[1][0]]}{emojis[printableMat[1][1]]}{emojis[printableMat[1][2]]}{emojis[printableMat[1][3]]} \n{emojis[printableMat[2][0]]}{emojis[printableMat[2][1]]}{emojis[printableMat[2][2]]}{emojis[printableMat[2][3]]} \n{emojis[printableMat[3][0]]}{emojis[printableMat[3][1]]}{emojis[printableMat[3][2]]}{emojis[printableMat[3][3]]}"
        else:
            return f"fuck you {message.author.name}, you cant do that"
    if p_message == 'd':
        if compareMatrixes(printableMat, right(deepcopy(printableMat))):
            printableMat = right(printableMat)
            printableMat = newNumberOnMat(printableMat)
            return f"{emojis[printableMat[0][0]]}{emojis[printableMat[0][1]]}{emojis[printableMat[0][2]]}{emojis[printableMat[0][3]]} \n{emojis[printableMat[1][0]]}{emojis[printableMat[1][1]]}{emojis[printableMat[1][2]]}{emojis[printableMat[1][3]]} \n{emojis[printableMat[2][0]]}{emojis[printableMat[2][1]]}{emojis[printableMat[2][2]]}{emojis[printableMat[2][3]]} \n{emojis[printableMat[3][0]]}{emojis[printableMat[3][1]]}{emojis[printableMat[3][2]]}{emojis[printableMat[3][3]]}"
        else:
            return f"fuck you {message.author.name}, you cant do that!"
    if p_message == 'reset':
        printableMat = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        printableMat = newNumberOnMat(printableMat)
        return None

    return message.content.upper()
