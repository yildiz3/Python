testList = [1, 2, 3, 4, 2, 2, 1, 4, 4,4, 4 ,4, 4]

xa = max(set(testList), key = testList.count)  

ya = testList.count(xa)

print("the most frequent number is" , xa, "and it was ",  ya, "times repeated")