from Crypto.Util import number
from math import gcd

import random
import multiprocessing 
print("Generating P and Q...")
p, q = number.getPrime(2048), number.getPrime(2048)
print("Generating N...")
n = p*q
print("Generating M and C...")
m, c = random.randint(0, n-1), random.randint(0, n-1)

print("Generating E...")
e = random.randint(3, n-1)

while not e % 2 == 0 and not gcd(p-1, q-1) == e:
    e = random.randint(3, n-1)
    # print(e)

# print(f"p: {p}\nq: {q}\nn: {n}\nm: {m}\nc: {c}\ne: {e}")
# print(e)
ans = 0
def getC(m, e, n):
    print(f"Generating C with values {m}, {e}, {n}")
    global ans
    ans += (m**e) % n

threads = []
for i in range(4):
    threads.append(multiprocessing.Process(target=getC, args=(m//4, e//4, n//4)))

for i in threads:
    i.start()

for i in threads:
    i.join()

print(ans)