# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 11:21:15 2018

@author: shivam
"""


def charToBinary(c):
    asci = ord(c)
    ans = ""
    while asci > 0:
        temp = asci % 2
        ans = chr(int(temp) + 48) + ans
        asci = asci // 2

    while len(ans) != 8:
        ans = '0' + ans

    return ans


def strToBlock(str):
    ans = []

    i = 0
    while i < len(str):
        temp = ""
        for j in range(8):
            if i + j >= len(str):
                temp += charToBinary("`")  # padding
            else:
                temp += charToBinary(str[i + j])

        ans.append(temp)
        i += 8

    return ans


def binToChar(binary):
    i = 7
    temp = 0
    po = 1
    while i >= 0:
        num = ord(binary[i]) - 48
        temp = temp + num * po
        po *= 2
        i -= 1

    return chr(temp)


def blockToStr(block):
    i = 0
    ans = ""
    while i < 64:
        ans += binToChar(block[i:i + 8])
        i += 8

    return ans


def initialPermutation(P):
    ans = ""

    pTable = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4, 62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48,
              40, 32, 24, 16, 8, 57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3, 61, 53, 45, 37, 29, 21,
              13, 5, 63, 55, 47, 39, 31, 23, 15, 7]

    for i in range(64):
        ans += P[pTable[i] - 1]

    return ans


def finalPermutation(P):
    ans = ""

    pTable = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4, 62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48,
              40, 32, 24, 16, 8, 57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3, 61, 53, 45, 37, 29, 21,
              13, 5, 63, 55, 47, 39, 31, 23, 15, 7]

    invPTable = [None] * 64

    for i in range(64):
        invPTable[pTable[i] - 1] = i + 1

    for i in range(64):
        ans += P[invPTable[i] - 1]

    return ans


def keyGeneration(Ckey, numberOfShift, roun):
    left = ""
    right = ""

    for i in range(56):
        if i < 28:
            left += Ckey[i]
        else:
            right += Ckey[i]
    # SHIFT LEFT
    for i in range(numberOfShift[roun]):
        temp1 = left[0]
        temp2 = right[0]
        templeft = left[1:]
        tempright = right[1:]
        templeft += temp1
        tempright += temp2
        left = templeft
        right = tempright

    key = left + right

    # COMPRESSION BOX
    pTable = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37,
              47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]

    temp = ""
    for i in range(48):
        temp += key[pTable[i] - 1]

    key = temp

    return key


def DESFunc(R, key):
    # EXPANSION
    temp = ""
    i = 0
    while i < 32:

        temp += R[(i - 1 + 32) % 32]
        for j in range(4):
            temp += R[i + j]
        temp += R[(i + 4) % 32]

        i += 4

    # MIXER

    temp2 = ""
    for i in range(48):
        if temp[i] == key[i]:
            temp2 += '0'
        else:
            temp2 += '1'

    temp = temp2

    # S BOX  (4*16)

    sTable = [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
              [0, 15, 7, 4, 14, 2, 13, 10, 3, 6, 12, 11, 9, 5, 3, 8],
              [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
              [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]]

    temp2 = ""

    i = 0
    while i < 48:

        rowNo = (ord(temp[i]) - 48) * 2 + ord(temp[i + 5]) - 48
        colNo = (ord(temp[i + 1]) - 48) * 8 + (ord(temp[i + 2]) - 48) * 4 + (ord(temp[i + 3]) - 48) * 2 + (
                    ord(temp[i + 4]) - 48)

        val = sTable[rowNo][colNo]

        x = ""

        while val > 0:
            temp1 = val % 2
            x = chr(temp1 + 48) + x
            val = val // 2

        while len(x) != 4:
            x = '0' + x

        temp2 += x
        i += 6

    temp = temp2

    # STRAIGHT P-BOX
    temp2 = ""
    pTable = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10, 2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6,
              22, 11, 4, 25]

    for i in range(32):
        temp2 += temp[pTable[i] - 1]

    temp = temp2

    return temp


def encrypt(text):
    blocks = strToBlock(text)

    Ckey = "10100010100101011110001111100011011111110000000000111101"  # 56 bits

    numberOfShift = []

    for i in range(16):
        if i == 0 or i == 1 or i == 8 or i == 15:
            numberOfShift.append(1)
        else:
            numberOfShift.append(2)

    for i in range(1, 16):
        numberOfShift[i] += numberOfShift[i - 1]
    myCipher = ""
    cipherBlocks = []
    for i in range(len(blocks)):

        P = blocks[i]

        P = initialPermutation(P)  # initial Permutation

        for roun in range(16):

            roundKey = keyGeneration(Ckey, numberOfShift, roun)

            L = ""
            R = ""
            for i in range(64):
                if i < 32:
                    L += P[i]
                else:
                    R += P[i]

            valueFromFunc = DESFunc(R, roundKey)

            # XORING L WITH VALUE FROM FUNCTION

            tempL = ""
            for i in range(32):
                if L[i] == valueFromFunc[i]:
                    tempL += '0'
                else:
                    tempL += '1'
            L = tempL

            # SWAPPING L AND R
            if roun != 15:
                temp = L
                L = R
                R = temp

            P = L + R

        P = finalPermutation(P)
        cipherBlocks.append(P)
        myCipher += blockToStr(P)

    return myCipher, cipherBlocks


def decrypt(cipherBlocks):
    Ckey = "10100010100101011110001111100011011111110000000000111101"  # 56 bits

    numberOfShift = []

    for i in range(16):
        if i == 0 or i == 1 or i == 8 or i == 15:
            numberOfShift.append(1)
        else:
            numberOfShift.append(2)

    for i in range(1, 16):
        numberOfShift[i] += numberOfShift[i - 1]

    blocks = []
    ans = ""
    for i in range(len(cipherBlocks)):

        P = cipherBlocks[i]

        P = initialPermutation(P)  # initial Permutation

        for roun in range(16):

            roundKey = keyGeneration(Ckey, numberOfShift, 15 - roun)

            L = ""
            R = ""
            for i in range(64):
                if i < 32:
                    L += P[i]
                else:
                    R += P[i]

            valueFromFunc = DESFunc(R, roundKey)

            # XORING L WITH VALUE FROM FUNCTION

            tempL = ""
            for i in range(32):
                if L[i] == valueFromFunc[i]:
                    tempL += '0'
                else:
                    tempL += '1'
            L = tempL

            # SWAPPING L AND R
            if roun != 15:
                temp = L
                L = R
                R = temp

            P = L + R

        P = finalPermutation(P)
        blocks.append(P)
        ans += blockToStr(P)

    toReturn = ""
    for c in ans:
        if c != '`':
            toReturn += c

    return toReturn


