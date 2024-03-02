D = int(input())
yobis = 0

while D > yobis:
    yobis = int(input())
    if D > yobis:
        D += yobis
    else:
        print(D)
        break
