from collections import Counter


class CompressStr():
    def __init__(self, st):
        self.st = st
        self.compress()
    def compress(self):
        st = self.st

        st = list(st)
        cout = sorted(list(Counter(st).items))

        