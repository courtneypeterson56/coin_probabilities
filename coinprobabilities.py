#Courtney Peterson
#CSCI2244: Randomness and Computation

from __future__ import print_function, division
import numpy as np  # this is a universal shorthand for numpy
import matplotlib.pyplot as plt

def run_lengths(n, p):
    """ Return a list of the run lengths in n tosses of a coin whose heads probability is p.
        Arguments:
        n--Number of tosses (a positive int),
        p--The probability of observing heads for any given toss (float between 0 and 1).
    """
    numpy_array = np.random.choice(['T', 'F'], p=[p, 1 - p], size=n) #returns a numpy array of T and Fs, with T= heads and F=tail
    run_lengthslist = []
    count = 1
    #print(numpy_array)  #don't necessarily need, but just shows sequence of tosses

    for i in range(0, len(numpy_array)-1):
        if numpy_array[i] == numpy_array[i + 1]:
            count +=1
        else:
            run_lengthslist.append(count)
            count = 1
    run_lengthslist.append(count)
    return run_lengthslist

def draw_hist_longest_run(n, p, trial_num, cumulative=False):
    """Draw a histogram of the maximum run length in n tosses of
        a coin with a heads probability p.
        Arguments:
        n--Number of tosses (a positive int),
        p--The probability of observing heads for any given toss
        (float between 0 and 1),
        trial_num--Number of trials used to create the histogram
        (positive int),
        cumulative--A flag to switch the histogram between cumulative
        and non-cumulative modes (bool).
        """
    total_runs_max = []
    for i in range(0, trial_num):
        x = run_lengths(n, p)
        y = max(x)
        total_runs_max.append(y)

    # "bins" for the histogram (bar chart). We get a column chart of the number
    # of elements in between each successive pair of bin markers.

    bins = np.arange(-.5, n + 1.5)
    fig = plt.figure()

    # setting zorder to 3 brings the histogram to the front
    plt.hist(total_runs_max, bins, color="g", cumulative=cumulative, zorder=3)
    plt.xlim(-1, 50)

    plt.title(('Max run length of {:d} tosses '.format(n) + 'of a coin {:d} times '.format(trial_num) +
               'with heads probability of {:}'.format(p)))
    plt.xlabel('Number of Heads')
    plt.ylabel('Number of Occurences')
    plt.grid(axis='both', zorder = 1) # push the grid lines to the back
    fig.savefig('Fig1.png')
    return None


def draw_hist_num_runs(n, p, trial_num, cumulative=False): ##need to FIX!
    """Draw a histogram of the number of runs in n tosses of a
    coin with a heads probability p.
    Arguments:
    n--Number of tosses (a positive int),
    p--The probability of observing heads for any given toss
    (float between 0 and 1),
    trial_num--Number of trials used to create the histogram
    (positive int),
    cumulative--A flag to switch the histogram between cumulative
    and non-cumulative modes (bool).
    """
    # n rows of k columns of coin tosses
    total_runs_len = []
    for i in range(0, trial_num):
        x = run_lengths(n, p)
        y = len(x)
        total_runs_len.append(y)

    # "bins" for the histogram (bar chart). We get a column chart of the number
    # of elements in between each successive pair of bin markers.
    bins = np.arange(-.5, n + 1.5)
    fig = plt.figure()

    # setting zorder to 3 brings the histogram to the front
    plt.hist(total_runs_len, bins, color="g", cumulative=cumulative, zorder=3)
    plt.xlim(-1, 50)
    plt.title(('{:d} tosses of '.format(n) + '{:d} coins with '.format(trial_num) +
                       'success probability {:}'.format(p)))
    plt.xlabel('Number of Runs')
    plt.ylabel('Number of Occurences')
    plt.grid(axis='both', zorder = 1) # push the grid lines to the back
    fig.savefig('Fig2.png')
    return None


draw_hist_longest_run(300, .5, 5000, cumulative=False)
plt.show()
#draw_hist_num_runs(50, .5, 5000, cumulative=False)
#draw_hist_num_runs(50, .2, 5000, cumulative=False)
#plt.show()
