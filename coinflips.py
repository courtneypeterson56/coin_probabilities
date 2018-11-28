#Courtney Peterson
#CSCI2244: Randomness and Computation

from __future__ import print_function, division
import numpy as np  # this is a universal shorthand for numpy
import matplotlib.pyplot as plt
import random

"""Used 5000 trials to estimate the probabilities of...

You flip a fair coin three times. Each flip is independent of the other flips.
This program determines the probability of each event described below.

1. The three flips have identical outcomes.
2. Exactly two flips have identical outcomes.
3. Exactly two consecutive flips have identical outcomes.
4. The sequence of flips consists of two heads and one tail.
5. The sequence of flips results in at least as many heads as tails.
6. Every flip has an outcome different from that of the flip immediately preceding it
    (except the first flip, which has no preceding flip).

To use simulations for estimating the probability of an
event, E, I ran n = 5000 trials and then counted the number of trials in which the event of interest,
E, occurs. This number is labeled nE. The ratio nE/n is an estimate for P(E)."""

def probability1(n, p):
    nE1 = 0
    nE2 = 0
    nE3 = 0
    nE4 = 0
    nE5 = 0
    nE6 = 0

    choices = ['HHH', 'HHT', 'HTH','HTT', 'THH', 'THT', 'TTH', 'TTT']
    numpy_array = np.random.choice(choices, n, p)
    print (numpy_array)

    for i in range(0, len(numpy_array)-1):
        if numpy_array[i][0] == numpy_array[i][1] == numpy_array[i][2]:
            nE1 +=1
    print ("The probability of three flips have identical outcomes:", nE1/n)

    for i in range(0, len(numpy_array)-1):
        if (numpy_array[i][0] == numpy_array[i][1]) or (numpy_array[i][0] == numpy_array[i][2]) or (numpy_array[i][1] == numpy_array[i][2]):
            nE2 +=1
            if numpy_array[i][0] == numpy_array[i][1] == numpy_array[i][2]:
                nE2 -=1
    print ("The probability of exactly two flips haveing identical outcomes:", nE2/n)

    for i in range(0, len(numpy_array)-1):
        if (numpy_array[i][0] == numpy_array[i][1]) or (numpy_array[i][1] == numpy_array[i][2]):
            nE3 +=1
            if numpy_array[i][0] == numpy_array[i][1] == numpy_array[i][2]:
                nE3 -=1
    print ("The probability of exactly two consecutive flips have identical outcomes:", nE3/n)

    for i in range(0, len(numpy_array)-1):
        if ((numpy_array[i]) == 'HHT'):
            nE4 +=1
        elif ((numpy_array[i]) == 'HTH'):
            nE4 +=1
        elif ((numpy_array[i]) == 'THH'):
            nE4 +=1
    print ("The probability of the sequence of flips consists of two heads and one tail:", nE4/n)

    for i in range(0, len(numpy_array)-1):
        if ((numpy_array[i]) == 'HHH'):
            nE5 +=1
        elif ((numpy_array[i]) == 'HHT'):
            nE5 +=1
        elif ((numpy_array[i]) == 'HTH'):
            nE5 +=1
        elif ((numpy_array[i]) == 'THH'):
            nE5 +=1
    print ("The probability of the sequence of flips results in at least as many heads as tails:", nE5/n)


    for i in range(0, len(numpy_array)-1):
        if (numpy_array[i][0] != numpy_array[i][1]) and (numpy_array[i][1] != numpy_array[i][2]):
            nE6 +=1
    print ("The probability of every flip has an outcome different from that of the flip immediately preceding it:", nE6/n)


probability1(5000, .5)


def probability2(n):
    nE7 = 0
    nE8 = 0
    nE9 = 0
    nE10 = 0
    word_array = []
    letters = 'abcdefg'

    for x in range(0, n):
        randomword = ''.join(random.choice(string.ascii_lowercase) for _ in range(5))
        word_array.append(randomword)
    print (word_array)


    for i in range(0, len(word_array)-1): ###FIX!!
        if (word_array[i][0]) in letters:
            if (word_array[i][1]) in letters:
                nE7 += 1
    print ("The probability that the first two characters are between a and g:", nE7/n)


    for i in range(0, len(word_array)-1):
        if (word_array[i][4]) == 'b':
            nE8 +=1
    print ("The probability that the last character is b:", nE8/n)


    #P(A) u P(B) = P(A) + P(B) - P(A n  B)
    nE9 = (nE8/n) + (nE7/n) - ((nE8/n) * (nE7/n))
    print ("The probability that the first two characters are between a and g or the last character is b:", nE9)


    #P(A) u P(B) = P(A) + P(B)
    nE10 = (nE8/n) + (nE7/n)
    print ("The probability that only one of the two events A or B occurs:", nE10)

probability2(5000)
