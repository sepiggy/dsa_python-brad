import time


def sumOfN2(n):
    start = time.time()

    theSum = 0
    for i in range(1, n+1):
        theSum += i

    end = time.time()

    return theSum, end-start


def sumOfN3(n):
    start = time.time()
    theSum = (n*(n+1))/2
    end = time.time()
    return theSum, end-start


print("sumOfN2 ---> Sum is %d required %10.7f seconds" % sumOfN2(100000))
print("sumOfN3 ---> Sum is %d required %10.7f seconds" % sumOfN3(100000))

print("sumOfN2 ---> Sum is %d required %10.7f seconds" % sumOfN2(1000000))
print("sumOfN3 ---> Sum is %d required %10.7f seconds" % sumOfN3(1000000))

print("sumOfN2 ---> Sum is %d required %10.7f seconds" % sumOfN2(10000000))
print("sumOfN3 ---> Sum is %d required %10.7f seconds" % sumOfN3(10000000))
