for i in range(100,1000):
    first = i // 100
    second = i // 10 % 10
    third = i % 10
    if i == first ** 3 + second ** 3 + third **3:
        print(i)
