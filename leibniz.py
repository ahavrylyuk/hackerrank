for _ in range(int(input())):
    print(sum((-1)**i/(2*i+1) for i in range(int(input()))))
