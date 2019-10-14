Clock.bpm = 110

# Fibonacci Rhythm
from functools import lru_cache
@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
    
fib_rhythm = [fib(n) % 9 for n in range(30)]

c1 >> charm(var([0,2,8]) + [0,2,8], dur = PDur(3,8),oct=[4,5]).every(3,"offadd",2)

k1 >> klank(var(4,6,9) + [1,0,1,1,1,1],rate = (4,12),oct=6)

p1 >> pluck(var([0,3,5,4]) + (0,2,4),dur=[3/4,1/2,1/4,1/2])
c1.stop()

p2 >> blip(var([1,4]) + [1,4,1,4,5,6])
k1.stop()

p1.solo()

p2.stop()

d1 >> play("-x--")

j1 >> jbass([4,5,8] + var([1,3,9,1,1,1,2,3]),dur=[1/3,1/4],amp=1)
p1.stop()

b2 >> pulse([fib_rhythm],dur=[1/3,1/4])
d1.stop()

b1 >> bass(amp=0.01)

Clock.bpm = 1

Clock.clear()