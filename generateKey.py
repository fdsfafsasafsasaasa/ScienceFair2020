from Crypto.Util import number
from math import gcd

import random
import multiprocessing 

class RSA:
    def __init__(self, procCount=4): 
        self.p, self.q = number.getPrime(2048), number.getPrime(2048)
        self.n = self.p*self.q
        self.m, self.c = random.randint(0, self.n-1), random.randint(0, self.n-1)
        self.e = random.randint(3, self.n-1)
        while not self.e % 2 == 0 and not gcd(self.p-1, self.q-1) == self.e:
            self.e = random.randint(3, self.n-1)
        self.procCount = procCount
        self.procs = []
        self.ans = 0

    def getCProcess(self):
        for proc in range(self.procCount):
            self.procs.append(multiprocessing.Process(target=self.getC, args=(self.m//4, self.e//4, self.n//4)))

        for proc in self.procs:
            proc.start()
        for proc in self.procs:
            proc.join()

        print(f"FINISHED: {self.ans}")

    def getC(self, m, e, n, ans=0):
        print(f"Generating C")
        self.ans += (m**e) % n

myKey = RSA(6)
myKey.getCProcess()