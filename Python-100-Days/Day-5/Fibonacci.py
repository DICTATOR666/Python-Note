def Fibo(n):
    if (n == 0):
        return 0
    if ((n == 1) | (n == 2)):
        return 1
    else:
        return Fibo(n-1) + Fibo(n-2)

for i in range(1,21):
     print(Fibo(i))
