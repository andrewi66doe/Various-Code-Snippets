class BinHeap:
    def __init__(self):
        self.heaplist = [0]
        self.current_size = 0

    def percup(self, i):
        while i // 2 > 0:
            if self.heaplist[i] < self.heaplist[i // 2]:
                tmp = self.heaplist[i]
                # Swap the elements
                self.heaplist[i] = self.heaplist[i // 2]
                self.heaplist[i // 2] = tmp
            i //= 2

    def min_child(self, i):
        if i * 2 + 1 > self.current_size:
            return i * 2
        else:
            if self.heaplist[i * 2] < self.heaplist[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def percdown(self, i):
        while (i * 2) <= self.current_size:
            mc = self.min_child(i)
            if self.heaplist[i] > self.heaplist[mc]:
                tmp = self.heaplist[i]
                self.heaplist[i] = self.heaplist[mc]
                self.heaplist[mc] = tmp
            i = mc

    def insert(self, item):
        self.heaplist.append(item)
        self.current_size += 1
        self.percup(self.current_size)

    def build_heap(self, list):
        i = len(list) // 2
        self.current_size = len(list)
        self.heaplist = [0] + list[:]

        while i > 0:
            self.percup(i)
            i -= 1


if __name__ == "__main__":
    h = BinHeap()
    h2 = BinHeap()
    l = [5, 13, 10, 9, 8, 12, 20, 11, 4, 3, 16, 7]
    h.build_heap(l)
    for elem in l:
        h2.insert(elem)
    print(h2.heaplist)
    print(h.heaplist)
