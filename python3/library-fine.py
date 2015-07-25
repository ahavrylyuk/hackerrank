actualD, actualM, actualY = map(int, input().split())
expectedD, expectedM, expectedY = map(int, input().split())

if actualY > expectedY:
    print(10000)
elif actualY == expectedY and actualM > expectedM:
    print(500 * (actualM - expectedM))
elif actualM == expectedM and actualD > expectedD:
    print(15 * (actualD - expectedD))
else:
    print(0)
