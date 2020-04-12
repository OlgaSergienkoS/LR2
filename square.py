import numpy as np
from myxml import downloadSquareFromXML, saveSquareInXml

class MagickSquare:

    def __init__(self, N = 1): #значение по умолчанию 
        self.N = N
        self.square = np.zeros((N,N), dtype=int)

    def download(self):
        self.N, self.square = downloadSquareFromXML()

    def save(self):
        saveSquareInXml(self.N, self.square)

    def ismagick(self):
        if np.amin(self.square) == 0:#проверяет на то, что если есть какой-то 0, то точно не магический 
            return False
        sq = np.copy(self.square)#создает копию массива
        sq = np.reshape(sq, self.N**2)#превращает в строчку
        sq.sort()#сортирует
        for i in range(1, self.N**2):#смотрим есть ли повторяющиеся элементы, если есть то не магический 
            if sq[i] == sq[i-1]:
                return False
        sum = self.N*(self.N**2 + 1)/2#формула магического квардрата
        if (np.sum(self.square, axis=0) == sum).all() and (np.sum(self.square, axis=1) == sum).all() and sum == np.diag(self.square).sum() and np.diag(np.fliplr(self.square)).sum() == sum:
            return True
        return False
