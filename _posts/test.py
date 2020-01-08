class MyRev():
    def __init__(self, seq):
        self.seq = seq
        self.len = len(seq)
        self.n = 0

    def seq2list(seq):
        list = []
        for i in seq:
            list.append(i)
        return list

    def __iter__(self):
        return self

    def __next__(self):
        temp = MyRev.seq2list(self.seq)
        if self.len == 0:
            raise StopIteration
        self.len -= 1
        return self.seq[self.len]


myRev = MyRev("FishC")
for i in myRev:
    print(i, end='')

