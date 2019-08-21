class Sorting:
    def mergesort(self, arr):
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
