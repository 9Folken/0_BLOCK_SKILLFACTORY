from time import time
import sys
sys.setrecursionlimit(1000000000)
 
def factorial(n):
    if n==0: return 1
    if n==1: return 1
    return factorial(n-1)*n
a = time()
for i in range(100):
    factorial(10000)
b = time()
print(b-a)
# Будет напечатано:
# 4.058465242385864