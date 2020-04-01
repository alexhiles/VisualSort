import numpy as np
import matplotlib.pylab as plt

class sort:

    def __init__(self, array):
        self.array    = array
        self.lenarray = len(self.array)

    def bubblesort(self):

        for i in np.arange(self.lenarray):

            for j in np.arange(self.lenarray - i - 1):

                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]

        return


    def part(self, arr, low, high):

        i = low - 1
        Pivot = arr[high]
        print(arr)
        for j in range(self.lenarray):

            if arr[j] <= Pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]

        return (i + 1)

    def quicksort(self):

        return
#        Pivot = self.array[-1]
#
#        i = 0
#
#        for j in np.arange(self.lenarray):
#
#            if self.array[j] > Pivot:






arr = [64, 34, 25, 122, 22, 11, 90]

x = sort(arr)

x.part(arr, 0, len(arr) - 1)

#x.bubblesort()
#x.quicksort()

print(x.array)
