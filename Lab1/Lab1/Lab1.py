
def StringMerge(str1, str2):
    result = [None] * (len(str1) + len(str2))
    #result = list(result)
    str1 = list(str1)
    str2 = list(str2)
    j = 0
    k = 0
    isStr1 = "true"
    for i in range(len(str1) + len(str2)):
        
        if(isStr1 == "true" and j < len(str1)):
            result[i] = str1[j]
            j += 1
            isStr1 = "false"
        else:
            if(k < len(str2)):
                result[i] = str2[k]
                k += 1
                isStr1 = "true"
            else:
                result[i] = str1[j]
                j += 1
    strResult = ''.join(result)
    return strResult
    

def ArmstrongNumber(num):
    numList = list([int(x) for x in str(num)])
    result = 0
    response = "No"
    for i in range(len(numList)):
       result += numList[i] ** len(numList)
    if(num == result):
        response = "Yes"
    else:
        response = "No"
    return response


stringMergeResult = StringMerge("day","time")
print(stringMergeResult)
armstrongNumberResult = ArmstrongNumber(371)
print(armstrongNumberResult)