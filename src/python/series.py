#!/bin/python3

# list of squares of natural numbers
sqr = [i**2 for i in range(100)]
print("{}\n".format(sqr))

# list of consecutive differences between elements of list(sqr)
sqdiff = [sqr[i]-sqr[i-1] for i in range(1, 100)]
print("{}\n".format(sqdiff))

# set of consecutive differences between elements of list(sqdiff)
sqdif2 = [sqdiff[i]-sqdiff[i-1] for i in range(1, 99)]

series = set(sqdif2)
print("{}\n".format(series))

