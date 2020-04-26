import numpy as np
from myxml import downloadSquareFromXML, saveSquareInXml

class MagickSquare:

    def __init__(self, N = 1): 
        self.N = N
        self.square = np.zeros((N,N), dtype=int)

    def download(self):
        self.N, self.square = downloadSquareFromXML()

    def save(self):
        saveSquareInXml(self.N, self.square)

    def ismagick(self):
        if np.amin(self.square) == 0:
            return False
        sq = np.copy(self.square)
        sq = np.reshape(sq, self.N**2)
        sq.sort()
        for i in range(1, self.N**2):
            if sq[i] == sq[i-1]:
                return False
        sum = self.N*(self.N**2 + 1)/2
        if (np.sum(self.square, axis=0) == sum).all() and (np.sum(self.square, axis=1) == sum).all() and sum == np.diag(self.square).sum() and np.diag(np.fliplr(self.square)).sum() == sum:
            return True
        return False
