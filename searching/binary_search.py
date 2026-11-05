def search(list, item):
    beginIndex = 0
    endIndex = len(list) - 1

    while beginIndex <= endIndex:
        midPoint = beginIndex + (endIndex - beginIndex) // 2
        midPointValue = list[midPoint]

        if midPointValue == item:
            return midPoint
        elif item <= midPointValue:
            endIndex = midPoint - 1
        else:
            beginIndex = midPoint + 1
    return None


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

print(search(list, 3))
print(search(list, 16))
print(search(list, 21))
