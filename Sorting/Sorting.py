class Sorting:
    def mergesort(self, arr):       # making a copied list
        if len(arr) is None or len(arr) == 1:
            return

        mid = len(arr) // 2  # floor of the division to be mid point
        L = arr[:mid]
        R = arr[mid:]
        self.mergesort(L)
        self.mergesort(R)

        i = j = k = 0
        # Copy the data to temp arr
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
        return arr

    def __swaparrpos(self, arr, pos1, pos2):
        arr[pos1], arr[pos2] = arr[pos2], arr[pos1]
        return arr


    def __quicksortutil(self, arr, posL, posR):
        if posR <= posL:
            return

        # print('Arr:{}'.format(arr))
        pivotpos = posL
        leftpos = posL + 1
        rightpos = posR

        # print('pivotpos:{} leftpos:{} rightpos:{}'.format(pivotpos, leftpos, rightpos))
        # print('arr[pivotpos]:{} arr[leftpos]:{} arr[rightpos]:{}'.format(arr[pivotpos], arr[leftpos], arr[rightpos]))

        while leftpos < rightpos:
            if arr[rightpos] > arr[pivotpos]:
                rightpos -= 1
                continue
            if arr[leftpos] <= arr[pivotpos]:
                leftpos += 1
                continue

            self.__swaparrpos(arr, leftpos, rightpos)

        if arr[pivotpos] > arr[leftpos]:
            self.__swaparrpos(arr, leftpos, pivotpos)
            pivotpos = leftpos

        self.__quicksortutil(arr, posL, pivotpos)
        self.__quicksortutil(arr, pivotpos+1, posR)


    def quicksort(self, arr):
        print('Array:{}'.format(arr))
        if len(arr) == 0 or len(arr) == 1:
            return arr

        self.__quicksortutil(arr, 0, len(arr)-1)
        return arr
