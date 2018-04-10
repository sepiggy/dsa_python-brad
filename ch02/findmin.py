# Self Check in chapter 2.3
import time
from random import randrange


def findMin(alist):
    '''
    O(n^2)
    '''
    overallmin = alist[0]
    operationnum = 0
    for i in alist:
        issmallest = True
        for j in alist:
            operationnum += 1
            if i > j:
                issmallest = False
        if issmallest:
            overallmin = i
    return overallmin, operationnum

#  print(findMin([5, 4, 3, 2, 1, 0]))
#  print(findMin([0, 4, 2, 1, 5, 3]))


def findMin2(alist):
    '''
    O(n)
    '''
    minsofar = alist[0]
    for anum in alist:
        if anum < minsofar:
            minsofar = anum
    return minsofar


# Benchmark
for listSize in range(1000, 10001, 1000):
    alist = [randrange(100000) for x in range(listSize)]

    start = time.time()
    minnum = findMin(alist)[0]
    end = time.time()

    start2 = time.time()
    minnum2 = findMin2(alist)
    end2 = time.time()
    print("min: %d, size: %d, time of O(n^2): %f s, time of O(n): %f s" %
          (minnum, listSize, end-start, end2-start2))
