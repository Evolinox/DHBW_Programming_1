def heronsMethod(n):
    x = int(n)

    while abs((x*x) - int(n)) > 0.01:
        x = (0.5)*((int(n)/x)+x)

    print("The square root is " + str(int(x)))